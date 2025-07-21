from PIL import Image

# 이미지 열기 및 변환
img = Image.open("ram.png")  # 너가 업로드한 이미지 이름
img = img.convert("1")  # 1bit 흑백화
img = img.resize((128, 64))  # OLED 사이즈로 맞춤

# 바이트 배열 추출 (왼쪽에서 오른쪽, 위에서 아래로)
data = bytearray(img.tobytes())

# 결과 출력 (복붙해서 micropython에 넣을 용도)
print("img = bytearray([")
for i in range(0, len(data), 16):
    line = ", ".join(f"0x{b:02X}" for b in data[i:i+16])
    print("    " + line + ",")
print("])")
