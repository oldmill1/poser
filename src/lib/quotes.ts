export const quotes = [
  "Today I went to the grocery store and forgot my reusable bags again. The cashier gave me that look, you know the one. I ended up carrying everything in my arms like some kind of grocery juggler.",
  
  "Local weather forecast calls for scattered showers this afternoon, with temperatures reaching a high of 72 degrees. The meteorologist on Channel 4 seems really excited about some low pressure system moving in from the west.",
  
  "My neighbor's dog has been barking for three hours straight. I'm starting to think it's learned Morse code and is trying to communicate something important. Maybe it's warning us about the mailman.",
  
  "The coffee shop on Main Street changed their Wi-Fi password again. It's now 'latte2024' which is at least better than last month's 'password123'. The barista said they change it every few weeks for security reasons.",
  
  "Traffic was terrible on the way to work this morning. There was construction on the bridge, and everyone was merging into one lane. I think I saw the same car three times in different positions. It was like a vehicular conga line.",
  
  "I tried to make pasta for dinner but somehow managed to burn the water. I didn't even know that was possible. The smoke alarm went off and now my apartment smells like a chemistry lab.",
  
  "The library is having a book sale this weekend. I told myself I wouldn't buy any more books until I finish the ones I already have, but that's never stopped me before. I have a problem.",
  
  "My phone died at 2 PM and I felt completely lost. I had to actually ask someone for directions, which felt like asking a stranger to help me tie my shoes. Technology has ruined my basic survival skills.",
  
  "The local news reported that someone found a wallet in the park with $50 in it and turned it in to the police station. Faith in humanity restored, at least until the next story about someone stealing parking meters.",
  
  "I spent twenty minutes looking for my keys this morning only to find them in the refrigerator. I have no memory of putting them there, but apparently past me thought it was a brilliant hiding spot."
];

export function getRandomQuote(): string {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  return quotes[randomIndex];
}
