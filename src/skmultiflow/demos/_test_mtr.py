from skmultiflow.core.pipeline import Pipeline
from skmultiflow.data.file_stream import FileStream
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.trees.regression_hoeffding_tree import RegressionHoeffdingTree


def demo(input_file, output_file=None):
    """ _test_mtr_regression

    This demo demonstrates how to evaluate a regressor. The data stream used
    is an instance of the RegressionGenerator, which feeds an instance from
    sklearn's SGDRegressor.

    Parameters
    ----------
    input_file: string
        A string describind the path for the input dataset

    output_file: string
        The name of the csv output file

    """
    # Setup the File Stream
    # stream = FileStream("../data/datasets/covtype.csv", -1, 1)
    # stream = WaveformGenerator()
    # stream.prepare_for_use()
    stream = FileStream(input_file, n_targets=16)
    stream.prepare_for_use()
    # Setup the classifier
    # classifier = SGDClassifier()
    # classifier = PassiveAggressiveClassifier()
    classifier = RegressionHoeffdingTree()
    # classifier = PerceptronMask()

    # Setup the pipeline
    pipe = Pipeline([('Classifier', classifier)])

    # Setup the evaluator
    evaluator = EvaluatePrequential(pretrain_size=1, batch_size=1, n_wait=200, max_time=1000,
                                    output_file=output_file, show_plot=False, metrics=['hamming_loss'])

    # Evaluate
    evaluator.evaluate(stream=stream, model=pipe)


if __name__ == '__main__':
    demo('../data/datasets/mtr/scm1d.csv', '/home/mastelini/Desktop/test_regression.csv')
