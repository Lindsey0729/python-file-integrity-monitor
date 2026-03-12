<h1>Python File Integrity Monitor</h1>

<hr>

<h2>Overview</h2>

<p>
This project demonstrates a <strong>File Integrity Monitoring (FIM)</strong> security tool built using Python.
</p>

<p>
The script monitors files within a specified directory and detects unauthorized modifications by comparing
file hashes against a stored baseline. If a file is modified or deleted, the program generates an alert.
</p>

<p>
File integrity monitoring is commonly used in <strong>Security Operations Centers (SOC)</strong> to detect:
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
  <li>SHA-256 hashing</li>
  <li>Host-based intrusion detection</li>
  <li>Security automation with Python</li>
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
</ul>

<p><strong>Example Output:</strong></p>

<pre>
Baseline created.
</pre>

<hr>

<h3>2. Continuous Monitoring</h3>

<ul>
  <li>The program continuously compares current file hashes against the stored baseline.</li>
</ul>

<p><strong>If a file is modified:</strong></p>

<pre>
[ALERT] File changed: test_file.txt
</pre>

<p><strong>If a file is deleted:</strong></p>

<pre>
[ALERT] File deleted: test_file.txt
</pre>

<hr>

<h2>Screenshots</h2>

<ul>
  <li>Baseline Creation</li>
  <li>File Change Detection</li>
  <li>File Deletion Detection</li>
</ul>

<hr>

<h2>How to Run the Program</h2>

<p><strong>Clone the repository:</strong></p>

<pre>
git clone https://github.com/YOURNAME/python-file-integrity-monitor.git
</pre>

<p><strong>Run the script:</strong></p>

<pre>
python file_integrity_monitor.py
</pre>

<hr>

<h2>Future Improvements</h2>

<ul>
  <li>Real-time monitoring using <code>watchdog</code></li>
  <li>Email alert notifications</li>
  <li>SIEM integration</li>
  <li>Windows Event Log monitoring</li>
</ul>
