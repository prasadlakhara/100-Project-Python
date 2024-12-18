import time

text = "The quick brown fox jumps over the lazy dog."
print("Typing Speed Test!")
print(f"Type this: \n{text}\n")

input("Press Enter to start...")
start_time = time.time()
typed_text = input("Your text: ")
end_time = time.time()

speed = len(typed_text) / (end_time - start_time) * 60  # Words per minute
accuracy = sum(1 for a, b in zip(typed_text, text) if a == b) / len(text) * 100

print(f"\nTyping Speed: {speed:.2f} characters per minute")
print(f"Accuracy: {accuracy:.2f}%")
