from client.Client import Client


if __name__ == "__main__":
    client = Client()
    client.start()

    while not client.should_close:
        client.poll_events()
        client.start_frame()
        client.update()
        client.draw()
        client.calculate_dt()

    client.quit()