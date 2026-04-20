from google import genai

API_KEY = "AQ.Ab8RN6KSQO_c5XcyvutVdM3RwVA82OSh8MeniYaKznHyS-g8tA"

client = genai.Client(api_key=API_KEY)

chat = client.chats.create(model="gemini-2.5-flash")

print("🤖 Чат-бот запущено! (Напишіть 'вихід' для завершення)")

while True:
    user_input = input("\nВи: ")

    if user_input.lower() in ['вихід', 'exit', 'quit', 'q']:
        print("🤖 Бот: До зустрічі! Роботу завершено.")
        break

    if not user_input.strip():
        continue

    try:
        response = chat.send_message(user_input)
        print(f"🤖 Бот: {response.text}")
    except Exception as e:
        print(f"❌ Виникла помилка: {e}")