import { json } from '@sveltejs/kit';
import { OpenAI } from 'openai';
import { env } from '$env/dynamic/private';
import type { RequestHandler } from './$types';

const openai = new OpenAI({
	apiKey: env.OPENAI_API_KEY
});

export const POST: RequestHandler = async ({ request }) => {
	try {
		const { message, isEdit } = await request.json();

		if (!message) {
			return json({ error: 'Message is required' }, { status: 400 });
		}

		let systemPrompt = '';
		let userMessage = message;

		if (isEdit) {
			systemPrompt = `You are a professional copy editor. Please perform a light/copy edit on the following text:

Light/Copy Edit Guidelines:
- Fix grammar, spelling, punctuation
- Ensure consistency in style and formatting
- Make minor clarity improvements
- Preserve the author's voice

Return your response in the following JSON format:
{
  "text": "the edited text here",
  "analysis": "Brief explanation of what changes were made, or if no changes were needed",
  "diff": "X characters added, Y characters removed (or 'no changes' if unchanged)"
}`;
		}

		const messages: Array<{ role: 'system' | 'user'; content: string }> = [];
		
		if (systemPrompt) {
			messages.push({
				role: 'system',
				content: systemPrompt
			});
		}
		
		messages.push({
			role: 'user',
			content: userMessage
		});

		const completion = await openai.chat.completions.create({
			model: env.MODEL || 'gpt-4o',
			messages,
			max_tokens: 1000,
			temperature: 0.3
		});

		const response = completion.choices[0]?.message?.content;

		if (!response) {
			return json({ error: 'No response from OpenAI' }, { status: 500 });
		}

		// For edit requests, parse the JSON response
		if (isEdit) {
			try {
				const parsedResponse = JSON.parse(response);
				return json({ 
					text: parsedResponse.text,
					analysis: parsedResponse.analysis,
					diff: parsedResponse.diff
				});
			} catch (parseError) {
				console.error('Failed to parse JSON response:', parseError);
				// Fallback to original response format if JSON parsing fails
				return json({ response });
			}
		}

		return json({ response });
	} catch (error) {
		console.error('OpenAI API error:', error);
		return json(
			{ error: 'Failed to get response from OpenAI' },
			{ status: 500 }
		);
	}
};
