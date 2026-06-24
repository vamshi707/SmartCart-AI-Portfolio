import cv2
import requests
import os


def download_image(url, filename):

    try:

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            with open(filename, "wb") as f:

                f.write(response.content)

            return filename

    except Exception as e:

        print("Download Error:", e)

    return None

def generate_room(room_image_path, products):

    room = cv2.imread(room_image_path)

    if room is None:
        print("Room image not found")
        return None

    height, width = room.shape[:2]

    for item in products:

        furniture_url = item.image

        temp_file = f"temp_{item.id}.png"

        furniture_path = download_image(
            furniture_url,
            temp_file
        )

        if not furniture_path:
            continue

        furniture = cv2.imread(
            furniture_path,
            cv2.IMREAD_UNCHANGED
        )

        if furniture is None:
            continue

        name = item.name.lower()

        # DYNAMIC SIZES

        if "bed" in name:

            fw = int(width * 0.40)
            fh = int(height * 0.40)

        elif "sofa" in name or "showcase" in name:

            fw = int(width * 0.70)
            fh = int(height * 0.70)

        elif "wardrobe" in name or "cupboard" in name or "office desk" in name :

            fw = int(width * 0.35)
            fh = int(height * 0.60)

        elif "table" in name:

            fw = int(width * 0.25)
            fh = int(height * 0.25)

   

        elif "lamp" in name:

            fw = int(width * 0.40)
            fh = int(height * 0.40)

        else:

            fw = int(width * 0.10)
            fh = int(height * 0.15)

        furniture = cv2.resize(
            furniture,
            (fw, fh)
        )

        # POSITION FROM DATABASE

        position = item.position.lower()

        if position == "left":

            x = 20
            y = height - fh - 50

        elif position == "right":

            x = width - fw - 20
            y = height - fh - 50

        elif position == "center":

            x = width // 2 - fw // 2
            y = height - fh - 40

        elif position == "corner":

            x = width - fw - 50
            y = height - fh - 80

        elif position == "wall":

            x = width - fw - 30
            y = height - fh - 120

        elif position == "front":

            x = width // 2 - fw // 2
            y = height - fh - 40

        elif position == "back":

            x = width // 2 - fw // 2
            y = int(height * 0.10)

        else:

            x = 50
            y = height - fh - 50

        # KEEP INSIDE IMAGE

        x = max(0, min(x, width - fw))
        y = max(0, min(y, height - fh))

        if len(furniture.shape) == 3 and furniture.shape[2] == 4:

            alpha = furniture[:, :, 3] / 255.0

            for c in range(3):

                room[
                    y:y+fh,
                    x:x+fw,
                    c
                ] = (

                    alpha * furniture[:, :, c]

                    +

                    (1 - alpha) *

                    room[
                        y:y+fh,
                        x:x+fw,
                        c
                    ]

                )

        else:

            room[
                y:y+fh,
                x:x+fw
            ] = furniture[:, :, :3]

    output_path = os.path.join(
        "media",
        "generated_room.jpg"
    )

    cv2.imwrite(
        output_path,
        room
    )

    return output_path