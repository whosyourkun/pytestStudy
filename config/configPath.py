import os

configPath = os.path.dirname(__file__)
projectPath = os.path.dirname(configPath)
dataPath = os.path.join(projectPath, "data")
testPath = os.path.join(dataPath, "test")
unitPath = os.path.join(testPath, "unit")