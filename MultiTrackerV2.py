import cv2

class MultiTracker:
    def __init__(self):
        self.trackers = []
    def add(self, tracker, frame, box):
        tracker.init(frame, box)
        self.trackers.append(tracker)
    def update(self, frame):
        boxes = []
        success = True
        for tracker in self.trackers:
            ok, box = tracker.update(frame)
            if ok:
                boxes.append(box)
            else:
                success = False
        return success, boxes

def MultiTracker_create():
    return MultiTracker()