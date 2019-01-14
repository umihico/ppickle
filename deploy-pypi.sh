git diff --cached --stat
staged_count=$(git diff --cached --numstat | wc -l)
zero="0"
if [ $staged_count = $zero ]; then
  echo "nothing is staged on git. exit."
  exit 1
fi
read -p 'commit message please:' commit_msg
script_dir=$(cd $(dirname $0); pwd)
parent_dirname=$(basename $script_dir)
project_name=$parent_dirname
python setup.py sdist bdist_wheel
twine upload dist/*
rm -rf dist
rm -rf build
rm -rf *.egg-info
rm -rf ${project_name}-*.*.*
version=$(cat version.txt)
git commit -m "version ${version} ${commit_msg}"
git push
