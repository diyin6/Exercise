import sys,time
def show_progress(has, total):

    rate_num = int(float(has) / float(total) * 100)
    sys.stdout.write("\r%3d%% |%s|" % (rate_num, ("#" * rate_num).ljust(100)))
    # sys.stdout.flush()


for i in range(50):
    show_progress(i + 1,50)
    time.sleep(0.1)