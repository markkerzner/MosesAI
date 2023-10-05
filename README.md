# MosesAI

1. To prepare your environment

```shell
wget https://elephantscale-public.s3.amazonaws.com/downloads/Anaconda3-2023.03-Linux-x86_64.sh
chmod +x Anaconda3-2023.03-Linux-x86_64.sh
./Anaconda3-2023.03-Linux-x86_64.sh
```
```
```shell
conda create --name MosesAI python=3.9
```

2. Setup the environment

```shell
conda activate MosesAI
pip install -r requirements.txt
```
The only think is that it often does not work and I install the packages mentioned in the `requirements.txt` manually

```shell
./requirements.sh
```

3. `Langchain_Semantic_Search_Pinecone.ipynb` is for storing the Pinecone index (done once and run locally)

4. Run on port 8080

```shell
./run_fastapi.sh
```