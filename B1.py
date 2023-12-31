import numpy
diff_cmd () {
	"$merge_tool_path" -wait -2 "$LOCAL" "$REMOTE" >/dev/null 2>&1
}

diff_cmd_help () {
	echo "Use Araxis Merge (requires a graphical session)"
}

merge_cmd () {
	if $base_present
	then
		"$merge_tool_path" -wait -merge -3 -a1 \
			"$BASE" "$LOCAL" "$REMOTE" "$MERGED" >/dev/null 2>&1
	else
		"$merge_tool_path" -wait -2 \
			"$LOCAL" "$REMOTE" "$MERGED" >/dev/null 2>&1
	fi
}

merge_cmd_help () {
	echo "Use Araxis Merge (requires a graphical session)"
}

translate_merge_tool_path() {
	echo compare
}
