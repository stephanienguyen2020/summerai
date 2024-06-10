# Summer AI
<a href="#license"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
[![Made with Python](https://img.shields.io/badge/Python->=3.10-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")

<img width="2562" alt="SummerAI_FigJam" src="https://github.com/stephanienguyen2020/summerai/assets/32094007/5aa2f7f5-b961-43ae-b35e-9d680d7fbb76">

This project aims to develop an artificial intelligence (AI) assistant to streamline the nurse visit process, saving time for both nurses, doctors, and patients.

## Motivation

Nurses in hospitals manage multiple patients daily and overwhelming workloads in high-stress environments. They often have to care for more patients than recommended, which leads to increased medical errors, burnout, and even patient mortality. According to Penn LDI, a single additional patient per nurse can raise the likelihood of patient mortality by 7% and significantly increase nurse burnout rates. Pixie AI aims to save nurses and doctors checkup time to focus more on patient's care.

## Project features

- **𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗲𝗱 𝗖𝗵𝗲𝗰𝗸-𝗜𝗻𝘀:** Before each check-in, SummerAI contacts patients via bedside intercoms, posing standardized questions. We made sure the AI sounds as natural and fast as possible. These interactions are recorded and analyzed for emotional and health cues (patient's mood, condition, note, etc), helping to prioritize care needs. This AI is using Gemini to generate responses.
- **𝗦𝗺𝗮𝗿𝘁 𝗥𝗮𝗻𝗸𝗶𝗻𝗴 𝗦𝘆𝘀𝘁𝗲𝗺:** Using sentiment analysis, our system evaluates the urgency of each patient's situation, ranking them to ensure nurses attend to the most critical cases first.
- **𝗥𝗲𝗮𝗹-𝗧𝗶𝗺𝗲 𝗨𝗽𝗱𝗮𝘁𝗲𝘀:** Nurses and doctors can check the order of their visit anytime. We prioritize patients who need urgent help first.
- **PDF record retrival:** Each patient will have a PDF record of their infomation and notes history.
- **Quick QR Checkin:** Each patient will have a QR code to quickly input their ID.
- **Simple UI**: We made simple UI with Streamlit for doctors/nurses to check their visit order and patient's records.
- **Alert system**: When a patient have high priority, the system will send an alert to corresponding doctor/nurse.

**Techstack:** Gemini, Hume AI, MongoDB, Streamlit, Resend, Python.

## Getting started

### Setting Up:

- Clone this repository
- Go to `terminal_backend`
- Create environment settings: `cp .env.example .env`
- Fill in the required environment variables in the `.env` file. Make sure you have MongoDB, Hume, Resend, and Google Gemini API Keys.
- Install required dependencies: `make install`

### Instructions: 
1. To create new patient or nurse, read `unit_test.py`, edit and run it.
2. Run the chat: `make chat`
3. Get the Streamlit UI: `make run`

- All PDF records will be saved in `records` folder.
- All QR code will be saved in `qr_code` folder.

## Contributing

We welcome contributions to this project! If you have experience in AI, NLP, or healthcare software development, feel free to:

Fork the repository and create a pull request with your contributions. Raise issues to report bugs or suggest improvements.

## License

<h2>License</h2>
Released under <a href="/LICENSE">MIT</a> by <a href="https://github.com/chrislevn">@chrislevn</a>.

## Disclaimer

This AI assistant is intended as a tool to support nurses and patients. It should not be used as a replacement for professional medical advice or diagnosis.
