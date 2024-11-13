const { Router } = require('express');
const { uploadFiles } = require('./uploadRoute');

const router = Router();

router.use('/upload', uploadFiles);

module.exports = router;
