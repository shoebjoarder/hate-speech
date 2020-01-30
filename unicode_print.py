text = "Brauchen ein gut ausgestattetes Milit\u00e4r - aber keine Aufr\u00fcstung \u00e0 la Trump! Geld, das Frau Merkel f\u00fcr Aufr\u00fcstung will, muss in die Bildung!"

print("\n" + text.encode('utf-8','surrogatepass').decode('utf-8') + "\n")