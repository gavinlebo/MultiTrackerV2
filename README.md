# MultiTrackerV2
A simple class/object to implement multiple trackers for multiple objects in OpenCV. Opposed to the built in MultiTracker class, MultiTrackerV2 is compatible with all trackers available in OpenCV..

## Usage
First, place the MultiTrackerV2.py file in the directory with your working file, then import it.
```python
import MultiTrackerV2 as MT
```
Next, create a MultiTrackerV2 object just like you would with the built in MultiTracker class.
```python
multiTracker = MT.MultiTracker_create()
```

To initialize the tracker, add all of the individual trackers and objects you would like the track, as well as the initial frame.
```python
for box in boxes:
  multiTracker.add(cv2.TrackerCSRT_create(), frame, box)
```

Finally, within your loop, update all the trackers at once to the newest frame with the update method.
```python
ret, box = multiTracker.update(frame)
```
