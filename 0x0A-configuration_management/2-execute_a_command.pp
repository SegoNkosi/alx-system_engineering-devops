# This code executes a command that kills a process
exec { 'killmenow':
	path		=> '/usr/bin/pkill killmenow',
	provider	=> 'shell',
	returns		=> [0, 1],
}

