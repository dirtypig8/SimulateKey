import xml.etree.ElementTree as ElementTree


class UtilityFunctions:
    @staticmethod
    def append_logo(root_node):
        ElementTree.SubElement(
            root_node,
            "content",
            attrib={
                "type": "logo"
            }
        )

    @staticmethod
    def append_text(root_node, value, codec, location, font_size, kerning, strike="normal"):
        ElementTree.SubElement(
            root_node,
            "content",
            attrib={
                "type": "text",
                "value": value,
                "codec": codec,
                "location": location,
                "font_size": font_size,
                "kerning": kerning,
                "strike": strike
            }
        )

    @staticmethod
    def append_single_qrcode(root_node, value, location):
        ElementTree.SubElement(
            root_node,
            "content",
            attrib={
                "type": "single_qrcode",
                "value": value,
                "location": location
            }
        )


    @staticmethod
    def append_start_print(root_node, cut_type):
        ElementTree.SubElement(
            root_node,
            "content",
            attrib={
                "type": "start_print",
                "cut_type": cut_type
            }
        )
