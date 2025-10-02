import { json } from '@sveltejs/kit';
import { OpenAI } from 'openai';
import { env } from '$env/dynamic/private';
import type { RequestHandler } from './$types';

const openai = new OpenAI({
	apiKey: env.OPENAI_API_KEY
});

export const POST: RequestHandler = async ({ request }) => {
	try {
		const { message, isEdit, editType } = await request.json();

		if (!message) {
			return json({ error: 'Message is required' }, { status: 400 });
		}

		let systemPrompt = '';
		let userMessage = message;

		if (isEdit) {
			let editGuidelines = '';
			
			switch (editType) {
				case 'light':
					editGuidelines = `Light/Copy Edit Guidelines:
- Fix grammar, spelling, punctuation
- Ensure consistency in style and formatting
- Make minor clarity improvements
- Preserve the author's voice`;
					break;
				case 'line':
					editGuidelines = `Line Edit Guidelines:
- Focuses on flow and readability at the sentence level
- Improves word choice and eliminates redundancy
- Enhances rhythm and pacing
- Strengthens transitions between paragraphs`;
					break;
				case 'developmental':
					editGuidelines = `Developmental/Structural Edit Guidelines:
- Big-picture analysis of content and organization
- Identifies plot holes (fiction) or logical gaps (non-fiction)
- Suggests restructuring chapters or sections
- Addresses pacing, character development, or argument strength
- May recommend adding or cutting entire sections`;
					break;
				default:
					editGuidelines = `Light/Copy Edit Guidelines:
- Fix grammar, spelling, punctuation
- Ensure consistency in style and formatting
- Make minor clarity improvements
- Preserve the author's voice`;
			}

			systemPrompt = `You are a professional editor. Your task is to EDIT and IMPROVE the provided text, NOT to answer questions or provide information about the topic.

IMPORTANT: Take the user's text and rewrite it to be clearer, more engaging, and better structured. Do NOT answer the question they're asking - instead, improve how they've asked it.

${editGuidelines}

Return your response in the following JSON format:
{
  "text": "the edited/improved version of their text",
  "analysis": "Brief explanation of what changes were made to improve the text",
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
