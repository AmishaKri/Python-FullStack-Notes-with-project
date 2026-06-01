from transformers import pipeline

pipe= pipeline("image-text-to-text", model="google/gemma-3-4b-it" )

messages=[
    {
        "role": "user",
        "content":[
            {"type": "image", "url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Good_Food_Display.jpg", "caption": "Hello, how are you?"},
            {"type": "text", "text": "What animal is on the candy?"}
        ]
    }
]

pip( text:messages)