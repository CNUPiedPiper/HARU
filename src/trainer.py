import sys
from trainer import trainer
import os.path


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(os.path.dirname(__file__))
        print '$python trainer.py model_number iteration_number'
        exit()

    t = trainer.Trainer()
    t.training(sys.argv[1], int(sys.argv[2]))
