r"""Configuration for language model experiment.

Usage:
    from lmp.config import BaseConfig

    config = BaseConfig(...params)
    config.save(path)
    config = config.load(path)
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import os

# 3rd-party modules

import torch

# self-made modules

import lmp.path


class BaseConfig:
    r"""Configuration for text-generation model.

    Attributes:
        batch_size:
            Training batch size.
            Must be bigger than or equal to `1`.
        checkpoint_step:
            Checkpoint interval based on number of mini-batch.
            Must be bigger than or equal to `1`.
        d_emb:
            Embedding dimension.
            Must be bigger than or equal to `1`.
        d_hid:
            Hidden dimension.
            Must be bigger than or equal to `1`.
        dataset:
            Name of the dataset to perform experiment.
            Must not be empty.
        dropout:
            Dropout rate.
            Must range from `0` to `1`.
        epoch:
            Number of training epochs.
            Must be bigger than or equal to '1'
        experiment:
            Name of the experiment.
            Must not be empty.
        is_uncased:
            Convert all upper case to lower case.
            Must be True or False.
        learning_rate:
            Optimizer's parameter `lr`.
            Must be bigger than `0`.
        max_norm:
            Max norm of gradient.
            Used when cliping gradient norm.
            Must be bigger than `0`.
        max_seq_len
            Maximum input sequence length.
            Must be bigger than `0`.
        min_count:
            Minimum of token'sfrequence.
            Used to filter words that is smaller than min_count.
        model_class:
            Language model's class.
        num_linear_layers
            Number of Linear layers.
            Must be bigger than or equal to `1`.
        num_rnn_layers:
            Number of rnn layers.
            Must be bigger than or equal to `1`.
        optimizer_class:
            Optimizer's class.
        seed:
            Control random seed.
            Must be bigger than `0`.
        tokenizer_class:
            Tokenizer's class.
    """

    def __init__(
            self,
            batch_size: int = 1,
            checkpoint_step: int = 500,
            dataset: str = '',
            d_emb: int = 1,
            d_hid: int = 1,
            dropout: float = 0.1,
            epoch: int = 10,
            experiment: str = '',
            is_uncased: bool = False,
            learning_rate: float = 1e-4,
            max_norm: float = 1,
            max_seq_len: int = 60,
            min_count: int = 0,
            model_class: str = 'lstm',
            num_linear_layers: int = 1,
            num_rnn_layers: int = 1,
            optimizer_class: str = 'adam',
            seed: int = 1,
            tokenizer_class: str = 'list'
    ):
        if not isinstance(batch_size, int):
            raise TypeError(
                '`batch_size`\'s type must be `int`.'
            )
        if batch_size < 1:
            raise ValueError(
                '`batch_size` must be bigger than or equal to `1`.'
            )
        if not isinstance(checkpoint_step, int):
            raise TypeError(
                '`checkpoint_step`\'s type must be `int`.'
            )
        if checkpoint_step < 1:
            raise ValueError(
                '`checkpoint_step` must be bigger than or equal to `1`.'
            )
        if not isinstance(d_emb, int):
            raise TypeError(
                '`d_emb`\'s type must be `int`.'
            )
        if d_emb < 1:
            raise ValueError(
                '`d_emb` must be bigger than or equal to `1`.'
            )
        if not isinstance(d_hid, int):
            raise TypeError(
                '`d_hid`\'s type must be `int`.'
            )
        if d_hid < 1:
            raise ValueError(
                '`d_hid` must be bigger than or equal to `1`.'
            )
        if not isinstance(dropout, float):
            raise TypeError(
                '`dropout`\'s type must be `float`.'
            )
        if not isinstance(dataset, str):
            raise TypeError(
                '`dataset`\'s type must be `str`.'
            )
        if not dataset:
            raise ValueError(
                '`dataset` must not be empty.'
            )
        if dropout < 0 or dropout > 1:
            raise ValueError(
                '`dropout` must range from `0` to `1`.'
            )
        if not isinstance(experiment, str):
            raise TypeError(
                '`experiment`\'s type must be `str`.'
            )
        if not experiment:
            raise ValueError(
                '`experiment` must not be empty.'
            )
        if not isinstance(epoch, int):
            raise TypeError(
                '`epoch`\'s type must be `int`.'
            )
        if epoch < 1:
            raise ValueError(
                '`epoch` must be bigger than or equal to `1`.'
            )
        if not isinstance(is_uncased, bool):
            raise TypeError(
                '`is_uncased`\'s type must be `bool`.'
            )
        if not isinstance(learning_rate, float):
            raise TypeError(
                '`learning_rate`\'s type must be `float`.'
            )
        if learning_rate < 0:
            raise ValueError(
                '`learning_rate` must be bigger than `0`.'
            )
        if not isinstance(max_norm, float):
            raise TypeError(
                '`max_norm`\'s type must be `float`.'
            )
        if max_norm < 0:
            raise ValueError(
                '`max_norm` must be bigger than `0`.'
            )
        if not isinstance(max_seq_len, int):
            raise TypeError(
                '`max_seq_len`\'s type must be `int`.'
            )
        if max_seq_len <= 0:
            raise ValueError(
                '`max_seq_len` must be bigger than `0`.'
            )
        if not isinstance(min_count, int):
            raise TypeError(
                '`min_count`\'s type must be `int`.'
            )
        if min_count < 1:
            raise ValueError(
                '`min_count` must be bigger than or equal to `1`.'
            )
        if not isinstance(model_class, str):
            raise TypeError(
                '`model_class`\'s type must be `str`.'
            )
        if not isinstance(num_linear_layers, int):
            raise TypeError(
                '`num_linear_layers`\'s type must be `int`.'
            )
        if num_linear_layers < 1:
            raise ValueError(
                '`num_linear_layers` must be bigger than or equal to `1`.'
            )
        if not isinstance(num_rnn_layers, int):
            raise TypeError(
                '`num_rnn_layers`\'s type must be `int`.'
            )
        if num_rnn_layers < 1:
            raise ValueError(
                '`num_rnn_layers` must be bigger than `1`.'
            )
        if not isinstance(optimizer_class, str):
            raise TypeError(
                '`optimizer_class`\'s type must be `str`.'
            )
        if not isinstance(seed, int):
            raise TypeError(
                '`seed`\'s type must be `int`.'
            )
        if seed < 0:
            raise ValueError(
                '`seed` must be bigger than `0`.'
            )
        if not isinstance(tokenizer_class, str):
            raise TypeError(
                '`tokenizer_class`\'s type must be `str`.'
            )

        self.batch_size = batch_size
        self.checkpoint_step = checkpoint_step
        self.d_emb = d_emb
        self.d_hid = d_hid
        self.dataset = dataset
        self.dropout = dropout
        self.epoch = epoch
        self.experiment = experiment
        self.is_uncased = is_uncased
        self.learning_rate = learning_rate
        self.max_norm = max_norm
        self.max_seq_len = max_seq_len
        self.min_count = min_count
        self.model_class = model_class
        self.num_linear_layers = num_linear_layers
        self.num_rnn_layers = num_rnn_layers
        self.optimizer_class = optimizer_class
        self.seed = seed
        self.tokenizer_class = tokenizer_class

    @classmethod
    def load(cls, experiment: str):
        r"""Load configuration JSON file.

        Args:
            experiment:
                Name of the existing experiment.
                Configuration file must be in JSON format.

        Raises:
            ValueError:
                If `experiment` is not type `str`.
            FileNotFoundError:
                If `experiment` does not exist.
            JSONDecodeError:
                If configuration is not in JSON format.
        """

        if experiment is None or not isinstance(experiment, str):
            raise TypeError('`experiment` must be type `str`.')

        file_path = os.path.join(
            lmp.path.DATA_PATH,
            experiment,
            'config.json'
        )

        if not os.path.exists(file_path):
            raise FileNotFoundError(f'file {file_path} does not exist.')

        with open(file_path, 'r', encoding='utf-8') as input_file:
            return cls(**json.load(input_file))

    def __iter__(self):
        r"""Make instance attributes iterable.

        Yields:
            All instance attributes.
        """
        yield 'batch_size', self.batch_size
        yield 'checkpoint_step', self.checkpoint_step
        yield 'd_emb', self.d_emb
        yield 'd_hid', self.d_hid
        yield 'dataset', self.dataset
        yield 'dropout', self.dropout
        yield 'epoch', self.epoch
        yield 'experiment', self.experiment
        yield 'is_uncased', self.is_uncased
        yield 'learning_rate', self.learning_rate
        yield 'max_norm', self.max_norm
        yield 'max_seq_len', self.max_seq_len
        yield 'min_count', self.min_count
        yield 'model_class', self.model_class
        yield 'num_linear_layers', self.num_linear_layers
        yield 'num_rnn_layers', self.num_rnn_layers
        yield 'optimizer_class', self.optimizer_class
        yield 'seed', self.seed
        yield 'tokenizer_class', self.tokenizer_class

    def save(self) -> None:
        r"""Save configuration into JSON file."""

        file_dir = os.path.join(
            lmp.path.DATA_PATH,
            self.experiment
        )
        file_path = os.path.join(
            file_dir,
            'config.json'
        )

        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(file_path, 'w', encoding='utf8') as output_file:
            json.dump(
                dict(self),
                output_file,
                ensure_ascii=False
            )

    @property
    def device(self):
        r"""Get running model device.

        If `torch.cuda.is_available() == True`, then run model on GPU.
        Else run model on CUDA device.

        Returns:
            Device create by `torch.device`.
        """
        if torch.cuda.is_available():
            return torch.device('cuda')
        return torch.device('cpu')
