echo 01. What is in this directory?
ls -a
echo

echo 02. Is Java installed?
java --version
echo

echo 03. Is Git installed?
git --version
echo

echo 04. What about build tools?
mvn --version
gradle --version
ant -version
echo

echo 05. Where is the Android SDK Root?
echo "$ANDROID_SDK_ROOT"
echo

echo 06. Where are the Selenium jars?
echo "$SELENIUM_JAR_PATH"
echo

echo 07. What is the Workspace location?
echo "$RUNNER_WORKSPACE"
echo

echo 08. Who is running this script?
whoami
echo

echo 09. How is the disc laid out?
df
echo

echo 10. What environment variables are available?
env