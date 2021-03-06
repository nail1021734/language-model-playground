r"""Language model with LSTM layers.

Usage:
    import lmp

    model = lmp.model.LSTMModel(...)
    logits = model(...)
    pred = model.predict(...)
"""

# built-in modules

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


# 3rd-party modules

import torch

# self-made modules

from lmp.model._base_rnn_model import BaseRNNModel


class LSTMModel(BaseRNNModel):
    r"""Language model with LSTM layers.

    Each input token will first be embedded into vectors, then project to
    hidden dimension. We then sequentially feed vectors into LSTM layer(s).
    Output vectors of LSTM layer(s) then go through fully-connected layer(s)
    and project back to embedding dimension in order to perform vocabulary
    prediction.

    Args:
        d_emb:
            Embedding matrix vector dimension. Must be bigger than or equal to
            `1`.
        d_hid:
            LSTM layers hidden dimension. Must be bigger than or equal to `1`.
        dropout:
            Dropout probability on all layers output (except output layer).
            Must range from `0.0` to `1.0`.
        num_linear_layers:
            Number of Linear layers to use. Must be bigger than or equal to
            `1`.
        num_rnn_layers:
            Number of LSTM layers to use. Must be bigger than or equal to `1`.
        pad_token_id:
            Padding token's id. Embedding layer will initialize padding
            token's vector with zeros. Must be bigger than or equal to `0`, and
            must be smaller than `vocab_size`.
        vocab_size:
            Embedding matrix vocabulary dimension. Must be bigger than or equal
            to `1`.

    Raises:
        TypeError:
            When one of the arguments are not an instance of their type annotation
            respectively.
        ValueError:
            When one of the arguments do not follow their constraints. See
            docstring for arguments constraints.
    """

    def __init__(
            self,
            d_emb: int,
            d_hid: int,
            dropout: float,
            num_linear_layers: int,
            num_rnn_layers: int,
            pad_token_id: int,
            vocab_size: int
    ):
        super().__init__(
            d_emb=d_emb,
            d_hid=d_hid,
            dropout=dropout,
            num_linear_layers=num_linear_layers,
            num_rnn_layers=num_rnn_layers,
            pad_token_id=pad_token_id,
            vocab_size=vocab_size
        )

        # Override RNN layer(s) with LSTM layer(s).
        if num_rnn_layers == 1:
            self.rnn_layer = torch.nn.LSTM(
                input_size=d_hid,
                hidden_size=d_hid,
                batch_first=True
            )
        else:
            self.rnn_layer = torch.nn.LSTM(
                input_size=d_hid,
                hidden_size=d_hid,
                num_layers=num_rnn_layers,
                dropout=dropout,
                batch_first=True
            )
