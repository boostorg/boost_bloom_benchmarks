# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; for Visual Studio builds,
`/arch:AVX2` is set, which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.10</td>
    <td align="right">4.37</td>
    <td align="right">3.43</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">10.99</td>
    <td align="right">10.56</td>
    <td align="right">16.54</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.00</td>
    <td align="right">4.20</td>
    <td align="right">4.29</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.93</td>
    <td align="right">5.72</td>
    <td align="right">5.73</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.80</td>
    <td align="right">15.59</td>
    <td align="right">17.32</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.82</td>
    <td align="right">4.91</td>
    <td align="right">4.82</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.00</td>
    <td align="right">8.84</td>
    <td align="right">8.83</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.72</td>
    <td align="right">18.82</td>
    <td align="right">16.77</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.45</td>
    <td align="right">5.27</td>
    <td align="right">5.43</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.06</td>
    <td align="right">13.67</td>
    <td align="right">13.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">27.05</td>
    <td align="right">24.39</td>
    <td align="right">16.68</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.18</td>
    <td align="right">6.07</td>
    <td align="right">5.89</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">12.21</td>
    <td align="right">15.85</td>
    <td align="right">15.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">8.01</td>
    <td align="right">10.62</td>
    <td align="right">10.64</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.81</td>
    <td align="right">4.98</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">6.10</td>
    <td align="right">5.68</td>
    <td align="right">5.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">3.69</td>
    <td align="right">4.74</td>
    <td align="right">4.72</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.41</td>
    <td align="right">5.51</td>
    <td align="right">5.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">11.27</td>
    <td align="right">8.99</td>
    <td align="right">8.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">16.26</td>
    <td align="right">10.52</td>
    <td align="right">8.50</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.29</td>
    <td align="right">6.21</td>
    <td align="right">6.24</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">11.09</td>
    <td align="right">11.64</td>
    <td align="right">11.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">9.06</td>
    <td align="right">10.56</td>
    <td align="right">6.09</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.63</td>
    <td align="right">6.61</td>
    <td align="right">6.61</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">13.31</td>
    <td align="right">14.72</td>
    <td align="right">14.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">30.51</td>
    <td align="right">17.31</td>
    <td align="right">6.49</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.47</td>
    <td align="right">10.61</td>
    <td align="right">16.48</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.14</td>
    <td align="right">4.25</td>
    <td align="right">4.33</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.18</td>
    <td align="right">5.88</td>
    <td align="right">5.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.67</td>
    <td align="right">15.17</td>
    <td align="right">17.04</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.85</td>
    <td align="right">4.75</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.03</td>
    <td align="right">8.72</td>
    <td align="right">8.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">20.05</td>
    <td align="right">20.58</td>
    <td align="right">17.33</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.61</td>
    <td align="right">5.99</td>
    <td align="right">7.01</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.30</td>
    <td align="right">13.21</td>
    <td align="right">13.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">35.09</td>
    <td align="right">33.29</td>
    <td align="right">18.58</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">9.40</td>
    <td align="right">7.18</td>
    <td align="right">7.74</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">12.40</td>
    <td align="right">20.82</td>
    <td align="right">19.40</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">8.14</td>
    <td align="right">10.81</td>
    <td align="right">10.81</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.95</td>
    <td align="right">5.11</td>
    <td align="right">5.06</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.30</td>
    <td align="right">5.79</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.87</td>
    <td align="right">4.66</td>
    <td align="right">4.74</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.50</td>
    <td align="right">5.40</td>
    <td align="right">5.44</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.86</td>
    <td align="right">9.19</td>
    <td align="right">9.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">19.63</td>
    <td align="right">11.00</td>
    <td align="right">9.46</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.95</td>
    <td align="right">6.15</td>
    <td align="right">6.40</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">11.21</td>
    <td align="right">11.98</td>
    <td align="right">11.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">12.04</td>
    <td align="right">16.41</td>
    <td align="right">8.70</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">7.40</td>
    <td align="right">8.79</td>
    <td align="right">8.07</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.10</td>
    <td align="right">19.88</td>
    <td align="right">17.08</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, X64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">27.96</td>
    <td align="right">4.84</td>
    <td align="right">4.10</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.62</td>
    <td align="right">8.16</td>
    <td align="right">14.70</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.14</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.16</td>
    <td align="right">5.27</td>
    <td align="right">5.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">12.61</td>
    <td align="right">12.63</td>
    <td align="right">16.25</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.69</td>
    <td align="right">4.37</td>
    <td align="right">4.39</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.02</td>
    <td align="right">8.29</td>
    <td align="right">8.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">16.70</td>
    <td align="right">15.72</td>
    <td align="right">15.37</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.23</td>
    <td align="right">4.93</td>
    <td align="right">4.95</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.24</td>
    <td align="right">12.52</td>
    <td align="right">12.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.53</td>
    <td align="right">19.79</td>
    <td align="right">15.78</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.78</td>
    <td align="right">5.60</td>
    <td align="right">5.77</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">13.66</td>
    <td align="right">12.87</td>
    <td align="right">12.86</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7421</td>
    <td align="right">3.29</td>
    <td align="right">3.94</td>
    <td align="right">3.95</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.75</td>
    <td align="right">4.37</td>
    <td align="right">4.35</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">4.74</td>
    <td align="right">5.14</td>
    <td align="right">5.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5384</td>
    <td align="right">2.73</td>
    <td align="right">3.54</td>
    <td align="right">3.53</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.36</td>
    <td align="right">5.33</td>
    <td align="right">5.10</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.15</td>
    <td align="right">8.44</td>
    <td align="right">8.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1163</td>
    <td align="right">10.52</td>
    <td align="right">6.09</td>
    <td align="right">4.79</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.92</td>
    <td align="right">5.92</td>
    <td align="right">5.97</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">10.39</td>
    <td align="right">13.34</td>
    <td align="right">12.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0286</td>
    <td align="right">5.99</td>
    <td align="right">6.76</td>
    <td align="right">4.51</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">5.43</td>
    <td align="right">6.41</td>
    <td align="right">6.41</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">14.41</td>
    <td align="right">14.70</td>
    <td align="right">14.90</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.50</td>
    <td align="right">19.89</td>
    <td align="right">12.89</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">11.05</td>
    <td align="right">10.61</td>
    <td align="right">16.27</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.74</td>
    <td align="right">4.42</td>
    <td align="right">4.46</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.80</td>
    <td align="right">7.05</td>
    <td align="right">7.29</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">16.66</td>
    <td align="right">17.56</td>
    <td align="right">17.35</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.71</td>
    <td align="right">5.28</td>
    <td align="right">5.83</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">10.78</td>
    <td align="right">11.72</td>
    <td align="right">11.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">43.64</td>
    <td align="right">31.27</td>
    <td align="right">16.80</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.48</td>
    <td align="right">8.17</td>
    <td align="right">6.63</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">15.56</td>
    <td align="right">15.60</td>
    <td align="right">16.11</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">39.28</td>
    <td align="right">40.33</td>
    <td align="right">17.76</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.07</td>
    <td align="right">9.16</td>
    <td align="right">11.21</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">19.12</td>
    <td align="right">19.30</td>
    <td align="right">22.90</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7269</td>
    <td align="right">4.02</td>
    <td align="right">4.67</td>
    <td align="right">4.65</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.15</td>
    <td align="right">4.86</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.64</td>
    <td align="right">6.65</td>
    <td align="right">6.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5394</td>
    <td align="right">3.09</td>
    <td align="right">4.04</td>
    <td align="right">4.50</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.82</td>
    <td align="right">5.90</td>
    <td align="right">5.66</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.32</td>
    <td align="right">11.11</td>
    <td align="right">10.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1161</td>
    <td align="right">15.35</td>
    <td align="right">13.29</td>
    <td align="right">11.07</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">6.84</td>
    <td align="right">9.11</td>
    <td align="right">7.49</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">13.47</td>
    <td align="right">17.93</td>
    <td align="right">17.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">13.05</td>
    <td align="right">19.34</td>
    <td align="right">10.68</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">11.43</td>
    <td align="right">11.46</td>
    <td align="right">11.84</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">20.53</td>
    <td align="right">21.57</td>
    <td align="right">21.94</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">21.80</td>
    <td align="right">5.29</td>
    <td align="right">3.81</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">7.78</td>
    <td align="right">5.05</td>
    <td align="right">12.60</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.63</td>
    <td align="right">1.34</td>
    <td align="right">1.33</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.54</td>
    <td align="right">1.98</td>
    <td align="right">1.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.04</td>
    <td align="right">10.54</td>
    <td align="right">15.12</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.11</td>
    <td align="right">2.74</td>
    <td align="right">2.20</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">3.13</td>
    <td align="right">3.42</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.83</td>
    <td align="right">13.05</td>
    <td align="right">17.90</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">2.54</td>
    <td align="right">3.52</td>
    <td align="right">2.23</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">10.51</td>
    <td align="right">7.81</td>
    <td align="right">6.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">21.31</td>
    <td align="right">13.07</td>
    <td align="right">15.25</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.27</td>
    <td align="right">2.15</td>
    <td align="right">3.15</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.20</td>
    <td align="right">4.88</td>
    <td align="right">4.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.39</td>
    <td align="right">2.03</td>
    <td align="right">2.02</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.79</td>
    <td align="right">1.53</td>
    <td align="right">1.45</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.54</td>
    <td align="right">1.97</td>
    <td align="right">2.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.23</td>
    <td align="right">1.61</td>
    <td align="right">2.12</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.91</td>
    <td align="right">1.77</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">4.03</td>
    <td align="right">3.48</td>
    <td align="right">2.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.73</td>
    <td align="right">3.90</td>
    <td align="right">2.89</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.06</td>
    <td align="right">1.89</td>
    <td align="right">1.91</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.07</td>
    <td align="right">4.20</td>
    <td align="right">3.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.58</td>
    <td align="right">4.17</td>
    <td align="right">2.38</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.16</td>
    <td align="right">1.86</td>
    <td align="right">1.84</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.46</td>
    <td align="right">4.73</td>
    <td align="right">5.21</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.89</td>
    <td align="right">19.46</td>
    <td align="right">11.10</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">26.83</td>
    <td align="right">22.70</td>
    <td align="right">33.39</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">10.81</td>
    <td align="right">6.52</td>
    <td align="right">9.19</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">7.33</td>
    <td align="right">10.22</td>
    <td align="right">8.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">47.79</td>
    <td align="right">36.98</td>
    <td align="right">26.12</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.31</td>
    <td align="right">6.38</td>
    <td align="right">8.93</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">12.75</td>
    <td align="right">12.57</td>
    <td align="right">13.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">82.15</td>
    <td align="right">58.18</td>
    <td align="right">32.59</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.87</td>
    <td align="right">9.57</td>
    <td align="right">11.94</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.29</td>
    <td align="right">17.19</td>
    <td align="right">17.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">81.20</td>
    <td align="right">58.54</td>
    <td align="right">26.96</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">13.37</td>
    <td align="right">10.96</td>
    <td align="right">11.15</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">24.59</td>
    <td align="right">22.47</td>
    <td align="right">25.85</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">4.07</td>
    <td align="right">5.25</td>
    <td align="right">5.63</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.04</td>
    <td align="right">3.43</td>
    <td align="right">3.20</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">5.07</td>
    <td align="right">5.40</td>
    <td align="right">4.21</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">6.77</td>
    <td align="right">8.07</td>
    <td align="right">7.78</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.93</td>
    <td align="right">8.36</td>
    <td align="right">8.13</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.51</td>
    <td align="right">12.95</td>
    <td align="right">12.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">17.70</td>
    <td align="right">20.12</td>
    <td align="right">14.34</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.60</td>
    <td align="right">10.92</td>
    <td align="right">9.27</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.76</td>
    <td align="right">13.69</td>
    <td align="right">12.44</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">12.89</td>
    <td align="right">15.99</td>
    <td align="right">9.94</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.56</td>
    <td align="right">6.96</td>
    <td align="right">8.78</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">22.82</td>
    <td align="right">19.68</td>
    <td align="right">19.80</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">34.51</td>
    <td align="right">5.52</td>
    <td align="right">3.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.01</td>
    <td align="right">12.49</td>
    <td align="right">17.07</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.79</td>
    <td align="right">4.18</td>
    <td align="right">4.19</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.86</td>
    <td align="right">5.53</td>
    <td align="right">5.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.43</td>
    <td align="right">17.51</td>
    <td align="right">17.57</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.91</td>
    <td align="right">4.73</td>
    <td align="right">4.88</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.56</td>
    <td align="right">8.34</td>
    <td align="right">8.48</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.56</td>
    <td align="right">21.16</td>
    <td align="right">17.00</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.55</td>
    <td align="right">5.27</td>
    <td align="right">5.37</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.54</td>
    <td align="right">10.70</td>
    <td align="right">10.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.94</td>
    <td align="right">27.06</td>
    <td align="right">16.96</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.88</td>
    <td align="right">5.88</td>
    <td align="right">5.87</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">19.61</td>
    <td align="right">14.26</td>
    <td align="right">14.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">8.86</td>
    <td align="right">10.01</td>
    <td align="right">10.02</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.96</td>
    <td align="right">5.17</td>
    <td align="right">5.23</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.16</td>
    <td align="right">5.52</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.85</td>
    <td align="right">4.87</td>
    <td align="right">4.08</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">7.96</td>
    <td align="right">5.79</td>
    <td align="right">5.86</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">19.47</td>
    <td align="right">8.65</td>
    <td align="right">8.63</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">8.36</td>
    <td align="right">10.05</td>
    <td align="right">5.39</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.26</td>
    <td align="right">6.54</td>
    <td align="right">6.52</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.87</td>
    <td align="right">10.30</td>
    <td align="right">10.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">9.31</td>
    <td align="right">9.87</td>
    <td align="right">5.60</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.34</td>
    <td align="right">7.44</td>
    <td align="right">7.68</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.81</td>
    <td align="right">12.55</td>
    <td align="right">13.63</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">44.00</td>
    <td align="right">21.15</td>
    <td align="right">8.19</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.64</td>
    <td align="right">13.16</td>
    <td align="right">17.80</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.00</td>
    <td align="right">4.45</td>
    <td align="right">4.63</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.40</td>
    <td align="right">6.25</td>
    <td align="right">6.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">25.89</td>
    <td align="right">22.03</td>
    <td align="right">18.88</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.47</td>
    <td align="right">6.22</td>
    <td align="right">6.47</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.31</td>
    <td align="right">10.08</td>
    <td align="right">10.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">37.93</td>
    <td align="right">34.88</td>
    <td align="right">19.58</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.15</td>
    <td align="right">8.89</td>
    <td align="right">8.92</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">23.87</td>
    <td align="right">16.69</td>
    <td align="right">17.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">69.04</td>
    <td align="right">74.94</td>
    <td align="right">22.77</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">18.94</td>
    <td align="right">11.14</td>
    <td align="right">12.39</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">31.78</td>
    <td align="right">22.88</td>
    <td align="right">24.42</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K,fast_multiblock32&ltK>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t, K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">8.96</td>
    <td align="right">10.14</td>
    <td align="right">10.14</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.86</td>
    <td align="right">5.54</td>
    <td align="right">5.63</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.54</td>
    <td align="right">6.27</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">4.13</td>
    <td align="right">5.97</td>
    <td align="right">4.86</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.91</td>
    <td align="right">6.92</td>
    <td align="right">6.91</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">22.19</td>
    <td align="right">10.73</td>
    <td align="right">12.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">11.87</td>
    <td align="right">15.51</td>
    <td align="right">10.03</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">12.92</td>
    <td align="right">9.39</td>
    <td align="right">9.35</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">21.94</td>
    <td align="right">14.74</td>
    <td align="right">14.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">16.72</td>
    <td align="right">20.57</td>
    <td align="right">14.84</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">18.45</td>
    <td align="right">16.16</td>
    <td align="right">15.61</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">31.69</td>
    <td align="right">21.71</td>
    <td align="right">22.83</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->
