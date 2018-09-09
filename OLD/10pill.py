from sklearn.datasets import fetch_lfw_people
lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

loop = get_event_loop()
while True:
    event = loop.get_event()
    process_event(event)