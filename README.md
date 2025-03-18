# News Research Tool

This tool is designed to streamline fact-finding and research by extracting relevant information from multiple news sources. Users provide a set of URLs along with a specific question, and the program analyzes the content to generate an answer based on the provided sources. By leveraging natural language processing (NLP) and information retrieval techniques, the tool ensures that responses are grounded in credible references. It is ideal for journalists, researchers, and analysts who need quick, source-backed insights without manually sifting through multiple articles.

## Cloning the Repository

To get started, clone this repository to your local machine using:

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

## Installing Dependencies

You can install the required dependencies using either `pip` or `conda`.

### Using `pip`

Ensure you have Python installed, then run:

```sh
pip install -r requirements.txt
```

### Using `conda`

If you prefer to use `conda`, create a new environment and install dependencies with:

```sh
conda create --name myenv python=3.11
conda activate myenv
conda install --yes --file requirements.txt
```

## Setting Up API Keys

To configure the OpenAI API key, create a `.env` file in the project root and add the following line:

```sh
echo "OPENAI_API_KEY='insert your api key here'" > .env
```

Alternatively, you can export the key as an environment variable:

```sh
export OPENAI_API_KEY='insert your api key here'
```

## Running the Project

Once the dependencies are installed and the environment is set up, you can start the project with:

```sh
streamlit run main.py
```

## Additional Notes
- Ensure your `.env` file is included in `.gitignore` to keep your API key secure.
- If using `conda`, make sure to activate the environment (`conda activate myenv`) before running the project.

For further details, refer to the project documentation or contact the maintainers.


