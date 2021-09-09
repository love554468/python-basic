import re

stringg = """1 var quotes [
2 'The Way Get Started Is To Quit Talking And Begin Doing. -Walt Disney',
'The Pessimist Sees Difficulty In Every Opportunity. The Optimist Sees The Opportunity In Every Difficulty. -Winston Churchill',
4 "Don 't Let Yesterday Take Up Too Much Of Today. Will Rogers',
5 "You Learn More From Failure Than From Success. Don't Let It Stop You. Failure Builds Character. - Unknown',
6 'It\'s Not Whether You Get knocked Down, It\'s Whether You Get Up. - Vince Lombardi',
7 'If You Are Working on Something That You Really Care About, You Don't Have To Be Pushed. The Vision Pulls You.- Steve Jobs',
8 'People Who Are Crazy Enough to Think They Can Change The World, Are The Ones Who Do.- Rob Siltanen',
9 'Failure Will Never Overtake Me If My Determination to Succeed Is Strong Enough. - Og Mandino',
10 'Entrepreneurs Are Great At Dealing With Uncertainty And Also Very Good At Minimizing Risk. That's The Classic Entrepreneur.- Mohnish Pabrai',
11 'We May Encounter Many Defeats But We Must Not Be Defeated. - Maya Angelou'
12 ]
13
{14 function newQuote() {
15 var randomNumber Math.floor(Math.random() * (quotes.length));
16 document.getElementById("quoteDisplay').innerHTML quotes[randomNumber];
}
17 }"""

str = "Sample 11 String 42 -In 2020"

pattern  = '[0-9]'
#match all digits in the strings and replace them by
#  empty string
mod_string = re.sub(pattern, '', str)

print(mod_string)