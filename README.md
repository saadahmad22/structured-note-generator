# structured-note-generator

## Introduction

- Have videos / audio, want notes
- We propose the development of a transcriber -> structured notes
- Should be able to remove irrelevant information
- Should be summarized

## Target Audience

- Students, people in meetings, anyone needing to condense video / audio to easily digestible text content

## Project Features + Description

- Group related information
- Process video to audio to text to structured notes to [human readable text]

## Tools/Technologies Used

- Flask, Python package for video to audio (ffmpeg/opencv), Python package for audio to text (pydub)
- OpenAI or self-built for summarizing / grouping
- HTML for document

## Evaluation

- Test pre-processing, basic testing of parent / child, inclusion of important elements, exclusion of irrelevant information
- LLM generated positive and negative examples for another LLM to judge our notes on (possibly a reach goal)