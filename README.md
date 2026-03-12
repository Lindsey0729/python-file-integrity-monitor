<h1>Python File Integrity Monitor</h1>

<p>
Python-based <strong>File Integrity Monitoring (FIM)</strong> tool that detects unauthorized
file modifications using <strong>SHA-256 hashing</strong>.
</p>

<hr>

<h2>Project Overview</h2>

<p>
This project demonstrates a <strong>File Integrity Monitoring (FIM)</strong> security tool built using Python.
The script monitors files within a specified directory and detects unauthorized modifications by comparing
file hashes against a stored baseline. If a file is modified or deleted, the program generates an alert.
</p>

<p>
File integrity monitoring is commonly used in a <strong>Security Operations Center (SOC)</strong> environment to detect:
</p>

<ul>
  <li>Malware activity</li>
  <li>Unauthorized file modification</li>
  <li>Configuration tampering</li>
  <li>Insider threats</li>
</ul>

<hr>

<h2>Security Concepts Demonstrated</h2>

<ul>
  <li>File Integrity Monitoring</li>
  <li>SHA-256 Hashing</li>
  <li>Host-Based Intrusion Detection</li>
  <li>Security Automation with Python</li>
</ul>

<hr>

<h2>Tools Used</h2>

<ul>
  <li>Python</li>
  <li><code>hashlib</code></li>
  <li><code>json</code></li>
  <li>OS file monitoring</li>
</ul>

<hr>

<h2>How It Works</h2>

<h3>1. Baseline Creation</h3>

<ul>
  <li>The program scans the target directory.</li>
  <li>It calculates <strong>SHA-256 hashes</strong> for each file.</li>
  <li>The hashes are stored as a baseline for future comparison.</li>
</ul>

<p><strong>Example Output:</strong></p>

<pre>
Baseline created.
</pre>

<hr>

<h3>2. Continuous Monitoring</h3>

<ul>
  <li>The program continuously scans the directory.</li>
  <li>It compares current file hashes against the stored baseline.</li>
</ul>

<p><strong>If a file is modified:</strong></p>

<pre>
[ALERT] File changed: test_file.txt
</pre>

<p><strong>If a file is deleted:</strong></p>

<pre>
[ALERT] File deleted: test_file.txt
</pre>
