#### TODOs for Building Protein Diffusion Model:

1. Data Collection:
    - AFDB:
        - This dataset is 23 TiB, this is likely too much for us to handle on this HPC.
        - https://github.com/google-deepmind/alphafold/blob/main/afdb/README.md has a guide on how to download it, in case it's something that'll be used in the future.
    - PDB:
        - I'm not sure how large PDB is yet. https://www.rcsb.org/stats/data_storage_growth suggests it's 1,437 GB for the 2024 version, which could be possible to work with on this HPC. Additionally, we only need `.mmCIF` files, so the download will likely be much smaller than what's listed.
        - https://www.rcsb.org/docs/programmatic-access/file-download-services has info for downloading using `rsync`, which would make things really convinient.
    - SAIR:
        - This company made a costructure dataset using Boltz-1 data.
        - Is appears to already be on HuggingFace https://huggingface.co/datasets/SandboxAQ/SAIR, which would make using it pretty easy.

    For now, it'll probably be best to start with PDB.

2. Data Curation:
    - Cluster data points by 40% similarity and collect the data points with the highest resolution in a cluster to act as a representative data point in the dataset.

3. Model Architecture:
    - Copy an existing model architecture (RoseTTAFold, FoldingDiff, Chroma, SimpleFold, Boltz).
    - GNNs and Transformers are often used for this.

4. Training:
    - Noise scheduler
    - Forward process
    - Reverse process

5. Inference:
    - Classifier guidance
    - Classifier free guidance
    - Physical constrained diffusion (https://www.biorxiv.org/content/10.1101/2025.10.15.682365v1.full.pdf)