const { Router } = require("express");
const multer = require("multer");

const uploadFiles = Router();

const { TranscriptionService } = require("../services/transcriptionService.js");
const trasncriptionService = new TranscriptionService();

const { OpenAIService } = require("../services/openAiService.js");
const openAIService = new OpenAIService();

const { DBService } = require("../services/dbService.js");
const dbService = new DBService();

const storage = multer.diskStorage({});
const upload = multer({ storage, dest: 'uploads/' });

uploadFiles.post("/file", upload.single('arquivo'), async function (req, res, next) {
    var arquivo = req.file;

    var transcricao = await trasncriptionService.transcribeAudioFromFile();
    console.log("terminou transcricao");

    var summarize = await openAIService.summarize();
    console.log("terminou sumário");

    await dbService.saveMetadataToDatabase();

    res.json({
        message: "resposta"
    });

});

uploadFiles.get('/health', async (_req, res, _next) => {

    const healthcheck = {
        uptime: process.uptime(),
        message: 'OK',
        timestamp: Date.now()
    };
    try {
        res.send(healthcheck);
    } catch (error) {
        healthcheck.message = error;
        res.status(503).send();
    }
});

module.exports = { uploadFiles };
