import time
from threading import Thread

import cv2 as cv
import numpy as np
from PIL import ImageGrab
from fishing.fishing_agent import FishingAgent

class MainAgent:
    def __init__(self) -> None:
        self.agents = []
        self.fishing_thread = None

        self.cur_img = None
        self.cur_imgHSV = None

        self.zone = "Feralas"
        self.time = "Nigth"


def update_screen(agent):
    # t0 = time.time()
    while True:
        screenshot = ImageGrab.grab()
        screenshot = np.array(screenshot)
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        screenshot_HSV = cv.cvtColor(screenshot, cv.COLOR_BGR2HSV)
        agent.cur_img = screenshot
        agent.cur_imgHSV = screenshot_HSV

        # cv.imshow("Computer Vision", agent.cur_img)
        # key = cv.waitKey(1)
        # if key == ord('q'):
        #     break
        # ex_time = time.time() - t0
        # print("FPS: " + str(1 / ex_time))
        # t0 = time.time()


def print_menu():
    print("Enter command:")
    print("\tS\tStart the main agent.")
    print("\tZ\tSet zone.")
    print("\tF\tStart the fishing agent.")
    print("\tQ\tQuit.")


if __name__ == "__main__":
    main_agent = MainAgent()

    print_menu()
    while True:
        user_input = input()
        user_input = str.lower(user_input).strip()

        if user_input == "s":
            update_screen_thread = Thread(
                target=update_screen,
                args=([main_agent]),
                name="Update screen thread",
                daemon=True
            )
            update_screen_thread.start()
            print("Thread started...")
        elif user_input == "z":
            pass
        elif user_input == "f":
            fishing_agent = FishingAgent(main_agent)
            fishing_agent.run()
        elif user_input == "q":
            break
        else:
            print("Input error.")
            print_menu()

    print("Done. Exiting application...")
