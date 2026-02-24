from PIL import Image

# --- Charger ton screenshot ---
screenshot = Image.open("BinaryWatch1.png")

# --- Créer une image 1024x500 fond noir ---
featured = Image.new("RGB", (1024, 500), "black")

# --- Calculer position pour centrer ---
x = (1024 - screenshot.width) // 2
y = (500 - screenshot.height) // 2

# --- Coller le screenshot sur le fond noir ---
featured.paste(screenshot, (x, y))

# --- Sauver le fichier final ---
featured.save("featured.png")

print("✅ Image générée : featured.png")
