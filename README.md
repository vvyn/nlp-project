# nlp project
prompt with $foodie

# bot start up
cd nlp-project
chatbot-env/Scripts/activate.bat
python chatbot.py

# questions
- query nlp data from wikidata? how do i know im getting high quality data?
- analyze full prompted sentence or just extract keywords? then get most similar queries that are not the same words and rec that to the user?

# hmm fix
- "salty or sweet" --> reponds with the first keyword in the if block
- else statement does not work
- get_data works with msg --> make sure to extract key words (how to do this effectively?)
- fix the sql query --> does not get many links