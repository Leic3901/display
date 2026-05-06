from PIL import Image

# ===== 参数 =====
INPUT_IMAGE = "input.png"
OUTPUT_MCFUNCTION = "the_storage.mcfunction"

# ===== 读取图片 =====
img = Image.open(INPUT_IMAGE).convert("RGBA")
w, h = img.size
pixels = img.load()

# ===== 展开像素（从下到上，左到右）=====
pixel_list = []

for y in range(h-1, -1, -1):  # 从下到上
    for x in range(w):        # 左到右
        r, g, b, a = pixels[x, y]
        int_color = ((a << 24) | (r << 16) | (g << 8) | b) & 0xFFFFFFFF

        if int_color >= 0x80000000:
            int_color -= 0x100000000

        pixel_list.append(f'{{I:{int_color}}}')

# 拼接 pixel 数据
pixel_data = "[" + ",".join(pixel_list) + "]"

# ===== 自动写入尺寸 =====
line1 = f'data merge storage minecraft:pixelart {{map:{{x:{w},y:{h}}},pixel:{pixel_data}}}'
line2 = "kill @e[type=marker,tag=pixel_art]"
line3 = "function ui:display/pixelart/pixelart"
# ===== 写入 mcfunction =====
with open(OUTPUT_MCFUNCTION, "w", encoding="utf-8") as f:
    f.write(line1 + "\n")
    f.write(line2 + "\n")
    f.write(line3 + "\n")


print(f"生成完成: {OUTPUT_MCFUNCTION}")
print(f"图片尺寸: {w} x {h}")





# from PIL import Image
#
# # ===== 参数 =====
# INPUT_IMAGE = "input.png"
# OUTPUT_MCFUNCTION = "the_storage.mcfunction"
#
# # ===== 读取图片 =====
# img = Image.open(INPUT_IMAGE).convert("RGB")
# w, h = img.size
# pixels = img.load()
#
# # ===== 展开像素（从下到上，左到右）=====
# pixel_list = []
#
# for y in range(h-1, -1, -1):  # 从下到上
#     for x in range(w):        # 左到右
#         r, g, b = pixels[x, y]
#
#         hex_color = f"#{r:02x}{g:02x}{b:02x}"
#         pixel_list.append(f'{{color:"{hex_color}"}}')
#
# # 拼接 pixel 数据
# pixel_data = "[" + ",".join(pixel_list) + "]"
#
# # ===== 自动写入尺寸 =====
# line1 = f'data merge storage minecraft:pixelart {{map:{{x:{w},y:{h}}},pixel:{pixel_data}}}'
# line2 = "kill @e[type=marker,tag=pixel_art]"
# line3 = "function ui:display/pixelart/pixelart"
# # ===== 写入 mcfunction =====
# with open(OUTPUT_MCFUNCTION, "w", encoding="utf-8") as f:
#     f.write(line1 + "\n")
#     f.write(line2 + "\n")
#     f.write(line3 + "\n")
#
#
# print(f"生成完成: {OUTPUT_MCFUNCTION}")
# print(f"图片尺寸: {w} x {h}")