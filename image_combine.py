from PIL import Image, ImageDraw, ImageFont
import textwrap

# 定义要添加到图像上的中文文本
chinese_text = """
三叔在一个多月后，准时的来到村中，要带韩立走了，临走前韩父反复嘱咐韩立，做人要老实，遇事要忍让，别和其他人起争执，而韩母则要他多注意身体，要吃好睡好。

在马车上，看着父母渐渐远去的身影，韩立咬紧了嘴唇，强忍着不让自己眼框中的泪珠流出来。

他虽然从小就比其他孩子成熟的多，但毕竟还是个十岁的小孩，第一次出远门让他的心里有点伤感和彷徨。他年幼的心里暗暗下定了决心，等挣到了大钱就马上赶回来，和父母再也不分开。

韩立从未想到，此次出去后钱财的多少对他已失去了意义，他竟然走上了一条与凡人不同的仙业大道，走出了自己的修仙之路。
"""

# 函数：按段落包装文本，保留原始缩进和换行
def wrap_text_by_paragraph(text, width):
    paragraphs = text.split('\n\n')
    wrapped_paragraphs = [
        '\n'.join(textwrap.wrap(paragraph, width=width//2, replace_whitespace=False))
        for paragraph in paragraphs
    ]
    return '\n\n'.join(wrapped_paragraphs)

# 定义文本和图片的边距
margin_size_text = 20  # 文本的边距
margin_size_img = 10  # 图片的边距

# 图片的路径（这里应该用你的图片路径替换）
image_path = '/Users/01417664/Downloads/p3.webp'

# 打开上传的图片
image = Image.open(image_path)

# 创建一个新的带有白色背景的图像
new_image = Image.new("RGB", (1024, 512), "white")

# 调整图片大小并粘贴到新图像的右侧，留出边距
resized_image = image.resize((512 - 2 * margin_size_img, 512 - 2 * margin_size_img))
new_image.paste(resized_image, (512 + margin_size_img, margin_size_img))

# 准备在图像上绘制文本
draw = ImageDraw.Draw(new_image)

# 使用支持中文的字体
font_path = "/System/Library/Fonts/PingFang.ttc"  # 用你的中文字体路径替换

# 定义初始字体大小
initial_font_size = 20

# 函数：调整字体大小和包装文本
def adjust_font_size_and_wrap_text(draw, text, font_path, max_width, max_height, initial_font_size):
    font_size = initial_font_size
    font = ImageFont.truetype(font_path, font_size)
    wrapped_text = wrap_text_by_paragraph(text, max_width // (font_size // 2))
    text_width, text_height = draw.multiline_textsize(wrapped_text, font=font)
    while font_size > 2 and (text_width > max_width or text_height > max_height):
        font_size -= 1
        font = ImageFont.truetype(font_path, font_size)
        wrapped_text = wrap_text_by_paragraph(text, max_width // (font_size // 2))
        text_width, text_height = draw.multiline_textsize(wrapped_text, font=font)
    return font, wrapped_text, (text_width, text_height)

# 第三部分：文本定位、绘制和图像保存

# 计算在考虑边距后的文本区域
available_text_width = 512 - 2 * margin_size_text
available_text_height = 512 - 2 * margin_size_text

# 调整字体大小并包装文本以适应新的边距
font, wrapped_text, text_size = adjust_font_size_and_wrap_text(
    draw, chinese_text, font_path, available_text_width, available_text_height, initial_font_size
)

# 计算文本块在可用文本区域中居中的位置
text_x = margin_size_text
text_y = margin_size_text + (available_text_height - text_size[1]) // 2

# 在图像上绘制经过调整边距的文本
draw.text((text_x, text_y), wrapped_text, font=font, fill="black")

# 将最终合成的图像保存到文件系统
final_image_path = './combined_3.jpg'
new_image.save(final_image_path)

print(f"Image saved to {final_image_path}")
