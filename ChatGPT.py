#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-

import os
import openai

class ChatGPT:

    def __init__(self, prompt):
        self.prompt = prompt

    def create_questions(self, fileName, amount=2):
        openai.api_key = os.getenv('OPEN_AI_API_KEY')

        out = []
        threshold = 2000
        for chunk in self.prompt.split('\n\n'):
            if out and len(chunk)+len(out[-1]) < threshold:
                out[-1] += ' ' + chunk
            else:
                out.append(chunk)
        print('Text splitted in ' + str(len(out)) + ' parts')
        
        index = 1
        for part in out:
            print('Prompt ' + str(index) + ' from ' + str(len(out)))
            
            chatgptPrompt = '''Create ''' + str(amount) + '''  multiple choice test questions based on the Text below.
            Each question can have 4 answers. 
            At least one answer must be correct.

            The Format should be like this:
            Question: What is the answer to this question?
            A) This is not the answer
            B) This is not the answer
            C) This is not the answer
            D) This is the answer
            Answer: D

            The Text:
            ''' + part + ''

            print('send ChatGPT Prompt')
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": chatgptPrompt}
                ]
            )

            content = completion.choices[0].message.content

            print('save ChatGPT Prompt result')
            print('__________________________')
            # write content in a json file in this folder
            with open('Data/' + fileName + '.text', 'a') as outfile:
                outfile.write(content + "\n\n")
                outfile.close()
            
            index += 1

