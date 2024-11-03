from PIL import Image, ImageDraw, ImageFont, ImageFilter

import string


# Map font characters to pixel coodinates

# Coordinates in X, Y, Rect then W, H

reference_rect = (500, 82, 762, 1262)
reference_center = (755, 690)

pixel_size = (10, 10)

# Hand Mapped
pixel_coordinates = [
    [(607, 669),(536, 550),(555, 420),(615, 310),(707, 230),(825, 200),(950, 180),],  # Strand 0
    [(620, 790),(490, 765),(439, 644),(430, 515),(430, 400),(455, 275),(525, 155),],  # Strand 1
    [(735, 850),(635, 930),(490, 915),(380, 835),(305, 740),(280, 605),(275, 480),],  # Strand 2
    [(850, 840),(820, 960),(719, 1040),(608, 1090),(408, 980),(360, 1045),(290, 950),],  # Strand 3
    [(910, 730),(970, 840),(960, 980),(890, 1100),(800, 1180),(680, 1240),(540, 1245),],  # Strand 4
    [(885, 600),(1015, 630),(1085, 740),(1110, 870),(1115, 1015),(1070, 1130),(1000, 1270),],  # Strand 5
    [(775, 535),(890, 460),(1020, 485),(1135, 550),(1200, 655),(1240, 780),(1240, 920),],  # Strand 6
    [(645, 560),(700, 450),(790, 365),(900, 335),(1015, 330),(1120, 370),(1210, 450),],  # Strand 7
]

center_led = (760,685) # Center LED, correspondes to bit 7 in strand 1, 2, 3 for (R, G, B)
center_off = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00'
center_on = [0, 128, 128, 0, 0, 0, 0, 0]

def map_pixel(input, target_size):
    return (input[0] - reference_rect[0]) * (target_size[0] / reference_rect[2]), (input[1] - reference_rect[1]) * (target_size[1] / reference_rect[3])

if __name__ == '__main__':
    image_size = (300, 500)
    rotation_degrees = 0 # ~60 degrees for first slot clockwise from the lanyard hole
        
    characters = list(string.ascii_uppercase + string.digits)

    for character in characters:
        # # Create a new image
        letter_image = Image.new('RGB', image_size, (255, 255, 255))

        pixel_image = Image.new('RGB', image_size, (255, 255, 255))

        # # Load a font
        font = ImageFont.truetype("LiberationSansNarrow-Bold.ttf", 400)

        label_font = ImageFont.truetype("LiberationSansNarrow-Bold.ttf", 10)

        # # Draw the text on the image
        draw_letter_image = ImageDraw.Draw(letter_image)

        draw_pixel_image = ImageDraw.Draw(pixel_image)

        draw_letter_image.text((150, 250), character, font=font, fill=(0, 0, 0), anchor='mm')

        letter_image.filter(ImageFilter.GaussianBlur(radius=50))
        letter_image = letter_image.rotate(rotation_degrees,
                                           center = (150,250),
                                           fillcolor=(255, 255, 255))

        pixel_count = 0

        character_bytes = [0] * 8

        # Center LED Handling

        pixel_coordinate = map_pixel(center_led, image_size)

        pixel_color = letter_image.getpixel(pixel_coordinate)

        if pixel_color != (255, 255, 255):
            for idx in range(len(character_bytes)):
                character_bytes[idx] = character_bytes[idx] | center_on[idx]

            draw_pixel_image.rectangle((pixel_coordinate[0] - pixel_size[0], pixel_coordinate[1] - pixel_size[1], pixel_coordinate[0] + pixel_size[1], pixel_coordinate[1] + pixel_size[1]), fill=(255, 0, 0))

            draw_letter_image.rectangle((pixel_coordinate[0] - pixel_size[0], pixel_coordinate[1] - pixel_size[1], pixel_coordinate[0] + pixel_size[1], pixel_coordinate[1] + pixel_size[1]), fill=(255, 0, 0))

            pixel_count += 1
        else:
            draw_letter_image.rectangle((pixel_coordinate[0] - pixel_size[0], pixel_coordinate[1] - pixel_size[1], pixel_coordinate[0] + pixel_size[1], pixel_coordinate[1] + pixel_size[1]), fill=(0, 255, 0))

        # Strand Pixels
        for strandidx, strand in enumerate(pixel_coordinates):
            for pixelidx, pixel in enumerate(strand):
                pixel_coordinate = map_pixel(pixel, image_size)

                if pixel_coordinate[0] < 0 or pixel_coordinate[1] < 0 or pixel_coordinate[0] > letter_image.size[0] or pixel_coordinate[1] > letter_image.size[1]:
                    continue

                # try:
                pixel_color = letter_image.getpixel(pixel_coordinate)

                if pixel_color != (255, 255, 255):
                    character_bytes[strandidx] = character_bytes[strandidx] | (1 << pixelidx)

                    # print(f'{strandidx} is now {character_bytes[strandidx]}')

                    draw_pixel_image.rectangle((pixel_coordinate[0] - pixel_size[0], pixel_coordinate[1] - pixel_size[1], pixel_coordinate[0] + pixel_size[1], pixel_coordinate[1] + pixel_size[1]), fill=(255, 0, 0))

                    draw_letter_image.rectangle((pixel_coordinate[0] - pixel_size[0], pixel_coordinate[1] - pixel_size[1], pixel_coordinate[0] + pixel_size[1], pixel_coordinate[1] + pixel_size[1]), fill=(255, 0, 0))

                    pixel_count += 1
                else:
                    draw_letter_image.rectangle((pixel_coordinate[0] - pixel_size[0], pixel_coordinate[1] - pixel_size[1], pixel_coordinate[0] + pixel_size[1], pixel_coordinate[1] + pixel_size[1]), fill=(0, 255, 0))

                # except:
                #     pass

                # draw.text(map_pixel(pixel, (300, 500)), f'{strandidx}{pixelidx}', font=label_font, fill=(255, 0, 0), anchor='mm')

        byte_string = ''.join([f'\\x{byte:02X}' for byte in character_bytes])

        print(f'\'{character}\': b\'{byte_string}\', ')

        # Save the image
        letter_image.save(f'letters/{character}-text.png')
        pixel_image.save(f'pixels/{character}-pixels.png')

        # print(f'{character}: {pixel_count} pixels')