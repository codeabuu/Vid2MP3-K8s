import pika, json

import pika.spec


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)

    except Exception as err:
        return ("Internal server error", 500)
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }
    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message), #converts to json str
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE, #makes sure msgs are retauned during pod crash

            ),
        )
    except:
        fs.delete(fid)
        return ("Internal Server Error!", 500)