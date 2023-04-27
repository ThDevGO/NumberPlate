import cv2
from detectPlate import plateDetect
import time

plateDetect = plateDetect.plateDetector()

VIDEO_CAMERA = 0

def camera(vid_path=0, img_path=None):
    if (img_path != None):
        pass
    if (vid_path != None):
        print(f'[INFO] Working with the video camera : {vid_path}')
        cap = cv2.VideoCapture(vid_path)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("No Camera Found.")
                time.sleep(1)
                cap = cv2.VideoCapture(vid_path)
                vid_path = vid_path + 1
                if(vid_path >= 4):
                    vid_path = 0
                continue
        
            # boxes = detector.detect(img)
            # message = boxes
            frame = cv2.resize(frame,(640,480))
            results = plateDetect.detectx(frame=frame)
            # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
            frame = plateDetect.plot_boxes(results, frame)
            cv2.imshow("Live View", frame)
            # vid_path = 1

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break
            
        ## closing all windows
        cv2.destroyAllWindows()

if __name__ == "__main__":
    camera(vid_path=VIDEO_CAMERA)