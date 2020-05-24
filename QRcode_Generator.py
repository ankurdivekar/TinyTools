import qrcode
from PIL import Image, ImageDraw, ImageFont


class QRCodeGenerator:

    def __init__(self):

        self.error_correction = qrcode.constants.ERROR_CORRECT_H
        # qrcode.constants.ERROR_CORRECT_L (Approx 7%)
        # qrcode.constants.ERROR_CORRECT_M (Approx 15%, default)
        # qrcode.constants.ERROR_CORRECT_Q (Approx 25%)
        # qrcode.constants.ERROR_CORRECT_H (Approx 30%)

        self.box_size = 10   #pixels
        self.border = 8     # boxes
        self.fill_color = 'black'
        self.back_color = 'white'

        self.mini_img_path = 'mini.jpg'
        self.mini_img_fraction = 0.28

    def get_qr_img(self, qr_data):

        # Configuration
        qr = qrcode.QRCode(
            error_correction=self.error_correction,
            box_size=self.box_size,
            border=self.border,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create QR code image
        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)
        width, height = img.size

        # Get mini image of calculated size
        mini_img_size = width*self.mini_img_fraction
        mini_img_size = int(mini_img_size - mini_img_size % self.box_size)
        img_mini = self.get_mini_img(self.mini_img_path, mini_img_size)

        # Calculate left top
        left_top = (width/2) - (mini_img_size/2)
        left_top = (int(left_top), int(left_top))

        # Create an RGB QR image
        rgb_img = Image.new("RGBA", img.size)
        rgb_img.paste(img)
        rgb_img.paste(img_mini, left_top)

        return rgb_img

    def save_qr_img(self, qr_data, img_path):
        img = self.get_qr_img(qr_data)
        img.save(img_path)

    def get_mini_img(self, img_path, im_size):
        self.mini_img_path = img_path
        im = Image.open(img_path)
        im.thumbnail((im_size, im_size))
        return im


if __name__ == "__main__":

    test_string = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed iaculis tempus cursus. ' \
                 'Nulla sed risus nisl. Ut gravida faucibus nulla. Quisque lorem nibh, egestas eu lorem nec, ' \
                 'rhoncus vestibulum metus. Maecenas et nulla tristique, cursus lectus eget, dictum dui. ' \
                 'Maecenas non scelerisque felis. In suscipit dui ut molestie porta. Vestibulum ante ipsum primis in ' \
                 'faucibus orci luctus et ultrices posuere cubilia curae; Nullam vitae semper risus, ut mattis dui. ' \
                 'Morbi eget tincidunt odio. Suspendisse imperdiet tristique nulla, et pellentesque nisi iaculis eget. ' \
                 'Fusce eget arcu cursus, iaculis ex vel, convallis metus. Maecenas aliquam tellus sem, id consequat ' \
                 'tellus convallis nec. Sed tristique arcu a posuere volutpat. Sed sed ex ut sapien sollicitudin ' \
                 'dapibus. Phasellus lacus augue, maximus sit amet placerat at, facilisis eget metus. Vivamus aliquam ' \
                 'accumsan eleifend. Duis sed purus lorem.'

    qrgen = QRCodeGenerator()
    img = qrgen.get_qr_img(test_string)
    img.show()
    # qrgen.save_qr_img(test_string, 'QR.png')


