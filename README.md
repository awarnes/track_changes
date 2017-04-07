# Track Changes:

##### This project is a test case to demonstrate the utilization of the Django signals framework to track all changes to models in a given project.


### Use:

The tracking app in the project is where the functions triggered by the signals live. There, the init.py helps to import the signals.py file which automatically registers listeners for all post_save and pre_delete signals.

#### post_save and pre_delete signals:

* Returns a sender (model), instance, and information about the instance that was saved.

#### Tracking methods:

* The track_create_and_update method:
 * makes sure that it is not tracking a TrackChange instance or an instance of a LogEntry,
 * creates a new TrackChange instance with pertinent data about which instance is being saved,
 * what changes have been made to it, if any,
 * and gives the tracking instance a time-stamp for the change.

* The track_delete method tracks:
 * whether a model has been deleted,
 * which model it is,
 * the instance primary key,
 * and what time it was deleted.

  Note: Since this method is registered through the pre_delete signal, it is able to get this information before actual deletion takes effect.


#### All model tracking:

By not specifying a specific sender for our receiver to listen to it automatically listens to every post_save and pre_delete signal that is sent in the project.

However, if we wanted to track only a specific set of models we can add that as a part of the receiver decorator as such:
        - @receiver(post_save, sender=[list-of-models])


#### Current Issues:

* On some related fields the primary key of the related object is not being passed through.
