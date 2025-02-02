Got it! Here's the updated README file with the script name changed to `test.py`:

---

# DeepSeek-R1 Local Testing with Agno

This repository demonstrates how to test the `deepseek-r1` model locally using the Agno framework and access it through an agent. In this example, we use the `Ollama` model for interaction.

### Prerequisites

- Python 3.x
- Agno package
- Ollama installed and running (or substitute your own model if needed)

### System Setup

#### 1. **Install Ollama**:

To use the `deepseek-r1` model, you need to have **Ollama** installed. Ollama allows you to run local large language models like `deepseek-r1`.

##### For **macOS**:
1. Download the [Ollama macOS installer](https://ollama.com/download).
2. Open the `.dmg` file and drag Ollama to your Applications folder.
3. After installation, you can verify it by running:
   ```bash
   ollama --version
   ```

##### For **Windows**:
1. Download the [Ollama Windows installer](https://ollama.com/download).
2. Run the installer and follow the setup instructions.
3. After installation, verify by running:
   ```bash
   ollama --version
   ```

##### For **Linux** (Ubuntu/Debian-based):
1. Download the appropriate Ollama package from the [Ollama website](https://ollama.com/download).
2. Alternatively, you can use the following commands to install it via the terminal:
   ```bash
   curl -sSL https://ollama.com/install | sh
   ```
3. After installation, verify it by running:
   ```bash
   ollama --version
   ```

#### 2. **Run DeepSeek-R1 with Ollama**:
Once you have Ollama installed, you need to start the `deepseek-r1` model.

Run the following command to start the model locally:

```bash
ollama run deepseek-r1
```

This command will load and start the `deepseek-r1` model. It will be ready to interact with once the model is initialized.

---

### Setup Instructions

1. **Install Dependencies**:

   Make sure you have all the necessary Python dependencies installed. You can install the required Python packages by running:

   ```bash
   pip install agno ollama
   ```

2. **Code Overview**:

   The following code snippet demonstrates how to configure and use the agent. The script is named `test.py`:

   ```python
   from agno.agent import Agent, RunResponse
   from agno.models.ollama import Ollama
   from typing import List

   # Initialize the agent with the deepseek-r1 model from Ollama
   agent = Agent(
       model=Ollama(id="deepseek-r1"),
       markdown=True
   )

   # Uncomment the line below to use a custom DeepSeek model if preferred
   # agent = Agent(model=DeepSeek(), markdown=True)

   # Request a response from the agent
   agent.print_response("Share a 2 sentence horror story.")
   ```

   In this code:
   - We import the necessary classes from `agno` and `ollama`.
   - We create an `Agent` instance with the `deepseek-r1` model by specifying its ID.
   - We ask the agent to generate a short horror story using the `print_response` method.

3. **Running the Code**:

   Once the environment is set up and `deepseek-r1` is running locally, you can execute the Python script to see how the model responds to your query. Simply run:

   ```bash
   python test.py
   ```

   You should see the agent's response printed in your terminal.

---

### Notes

- By default, this setup uses the `Ollama` model, which you can replace with any other compatible model.
- If you wish to experiment with a different model or use the original `DeepSeek`, simply comment/uncomment the relevant lines.

---

### Contributing

Feel free to fork this repository and submit issues or pull requests if you have any improvements or fixes!

---

Now, the README refers to the script as `test.py` as per your request. Let me know if you'd like to make any other adjustments!