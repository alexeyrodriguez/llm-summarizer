from llm_utils import SummarySpec

preprocess_spec = SummarySpec(
    """
If there is information related to how the data was preprocessed for training,
please extract the text verbatim, be concise and do not add text that is not in the paper.
""",
    """
Please consider the data preprocessing details for training provided in the context below
and provide an overall summary for the preprocessing.
""",
    "preprocessing",
)

training_spec = SummarySpec(
    """
If there is information related to how the neural network was trained
(for example batch size, learning rate, number of epochs, losses),
please extract the text verbatim, be concise and do not add text that is not in the paper.
""",
    """
Please consider the details for neural network training provided in the context below
and provide an overall summary for the training procedure and hyperparameters.
""",
    "training",
)

dataset_spec = SummarySpec(
    """
If there is information related to what dataset was used to train the neural network,
please extract the text verbatim, be concise and do not add text that is not in the paper.
""",
    """
Please consider the details for the dataset used in the neural network training provided in the context below
and provide an overall summary for the dataset used.
""",
    "dataset",
)

architecture_spec = SummarySpec(
    """
If there is information related to the neural network architecture,
please extract the text verbatim, be concise and do not add text that is not in the paper.
""",
    """
Please consider the neural network details provided in the context below
and provide an overall summary for it.
""",
    "architecture",
)

evaluation_spec = SummarySpec(
    """
If there is information related to the evaluation of the neural network (for example metrics, results, comparisons),
please extract the text verbatim, be concise and do not add text that is not in the paper.
""",
    """
Please consider the neural network evaluation details (e.g. metrics, results, comparisons) provided in the context below
and provide an overall summary for it.
""",
    "evaluation",
)

summary_spec = SummarySpec(
    None,
    """
Please consider the machine learning paper provided in the context below
and provide an overall summary for it.
""",
    "summary",
    2,
)


all_specs = [summary_spec, preprocess_spec, training_spec, dataset_spec, architecture_spec, evaluation_spec]