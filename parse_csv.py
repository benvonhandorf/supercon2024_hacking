import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageFilter

pixel_range = (49856.001, 28632.299, 51141.999, 30361.0)
base_size = (pixel_range[2] - pixel_range[0], pixel_range[3] - pixel_range[1])

def map_pixel(pixel, image_size):
    return (int((pixel[0] - pixel_range[0]) * (image_size[0] / base_size[0])), 
            int((pixel[1] - pixel_range[1]) * (image_size[1] / base_size[1])))

if __name__ == '__main__':
    img_pixels = Image.new('RGB', (300, 500), (255, 255, 255))
    draw_pixels = ImageDraw.Draw(img_pixels)

    df = pd.read_csv('pnp.csv')
    
    df['Mid X'] = df['Mid X'].str.replace('mil', '').astype(float)
    df['Mid Y'] = df['Mid Y'].str.replace('mil', '').astype(float)
    
    filtered_df = df[df['Designator'].str.contains('LED', na=False)]
    print(filtered_df)

    for index, row in filtered_df.iterrows():
        pixel_loc = map_pixel((row['Mid X'], row['Mid Y']), (300, 500))
        print(f'\'{row["Designator"]}\' : ({pixel_loc[0]}, {pixel_loc[1]}),')

    # print(f'({df["Mid X"].min()}, {df["Mid Y"].min()}, {df["Mid X"].max()}, {df["Mid Y"].max()})')