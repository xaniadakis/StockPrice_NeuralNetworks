import argparse

class ArgumentParser():
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', type=str, default=None)
        parser.add_argument('-n', type=int, default=10)
        parser.add_argument('-q', type=str, default=None)
        parser.add_argument('-od', type=str, default="output_dataset.pkl")
        parser.add_argument('-oq', type=str, default="output_query_file.pkl")
        parser.add_argument('-mae', type=float, default=None)
        parser.add_argument('-batch_size', type=int, default=3)
        parser.add_argument('-num_layers', type=int, default=4)
        parser.add_argument('-layers_size', type=tuple, default=(1,1))
        parser.add_argument('-num_epochs', type=int, default=100)

        args = parser.parse_args()
        self.dataset = args.d
        self.queryset = args.q
        self.output_dataset_file = args.od
        self.output_query_file = args.oq
        self.error_value_as_double = args.mae
        self.number_of_time_series_selected = args.n
        self.look_back=1
        self.num_layers = args.num_layers
        self.batch_size = args.batch_size
        self.layers_size = args.layers_size
        self.num_epochs = args.num_epochs