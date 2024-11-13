// Load the .env file if it exists
const { AzureOpenAI } = require("openai");

class OpenAIService {

  async summarize(text) {
    var command = ``;
    return this.query(text, command);
  }

  async query(prompt, command) {
    var apiKey = "7c18f21f1ddf42ebb3e6c144e7fe73ed";
    var endpoint = "https://openai-conarec.openai.azure.com/";
    var apiVersion = "2024-05-01-preview";
    var deployment = "conarec-35";

    console.log("== Get completions Sample ==");
    var client = new AzureOpenAI({ endpoint, apiKey, apiVersion, deployment });
    var result = await client.chat.completions.create({
      messages: [
        { role: "system", content: prompt },
        { role: "user", content: command }
      ],
      model: '',
      temperature: 0.2
    });

    for (var choice of result.choices) {
      return choice.message;
    }
  }
}

module.exports = { OpenAIService };
