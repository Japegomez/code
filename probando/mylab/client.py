from flask_babel import gettext
from weblablib import weblab_user
from mylab import weblab, redis
from mylab.hardware import program_device

LIGHTS = 2




def client_status():
    "Return the status of the client"
    # A pipeline in Redis is a single connection, that run with
    # transaction=True (the default), it runs all the commands in a single
    # transaction. It's useful to get all the data in once and to peform
    # atomic operations
    pipeline = redis.pipeline()

    for light in range(LIGHTS):
        pipeline.get('client:lights:{}'.format(light))

    pipeline.get('hardware:microcontroller:programming')
    pipeline.get('hardware:microcontroller:state')

    # Now it's run
    results = pipeline.execute()

    lights_data = {
        # 'light-1': True
    }

    for pos, light_state in enumerate(results[0:LIGHTS]):
        lights_data['light-{}'.format(pos+1)] = light_state == 'on'

    programming, state = results[LIGHTS:]
    if programming is not None:
        microcontroller = gettext('Programming: %(step)s', step=programming)
    elif state == 'empty':
        microcontroller = gettext("Empty memory")
    elif state == 'failed':
        microcontroller = gettext("Programming failed")
    elif state == 'programmed':
        microcontroller = gettext("Programming worked!")
    else:
        microcontroller = gettext("Invalid state: %(state)s", state=state)

    task = weblab.get_task(program_device)
    if task:
        print("Current programming task status: %s (error: %s; result: %s)" %
              (task.status, task.error, task.result))

    return dict(lights=lights_data, microcontroller=microcontroller, time_left=weblab_user.time_left)
