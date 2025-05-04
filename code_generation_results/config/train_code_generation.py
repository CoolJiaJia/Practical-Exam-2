# train a character-level model on Python code dataset

out_dir = 'out-code-generation'
eval_interval = 250
eval_iters = 100
log_interval = 50

# we'll train on larger context to better handle code structure
wandb_log = False
wandb_project = 'code-generation'
wandb_run_name = 'code-gpt'

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 64
block_size = 512  # longer context for code

# model configuration - larger than shakespeare model
n_layer = 8
n_head = 8
n_embd = 512
dropout = 0.2

learning_rate = 5e-4
max_iters = 5000
lr_decay_iters = 5000
min_lr = 1e-5
beta2 = 0.99

warmup_iters = 100
device = 'cuda' if torch.cuda.is_available() else 'cpu'
compile = False  # disable PyTorch 2.0 compilation
