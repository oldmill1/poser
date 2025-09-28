export const quotes = [
  "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles.",
  
  "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity.",
  
  "In the beginning was the Word, and the Word was with God, and the Word was God. He was with God in the beginning.",
  
  "Call me Ishmael. Some years ago—never mind how long precisely—having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world.",
  
  "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",
  
  "The way to get started is to quit talking and begin doing. The future belongs to those who believe in the beauty of their dreams.",
  
  "Two roads diverged in a yellow wood, and sorry I could not travel both and be one traveler, long I stood and looked down one as far as I could to where it bent in the undergrowth.",
  
  "I have a dream that one day this nation will rise up and live out the true meaning of its creed: 'We hold these truths to be self-evident, that all men are created equal.'",
  
  "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle.",
  
  "In three words I can sum up everything I've learned about life: it goes on. The woods are lovely, dark and deep, but I have promises to keep, and miles to go before I sleep."
];

export function getRandomQuote(): string {
  const randomIndex = Math.floor(Math.random() * quotes.length);
  return quotes[randomIndex];
}
