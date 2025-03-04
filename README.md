# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for six different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
which causes `fast_multiblock32` to use its AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

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
    <td align="right">26.39</td>
    <td align="right">4.57</td>
    <td align="right">3.53</td>
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
    <td align="right">11.18</td>
    <td align="right">10.72</td>
    <td align="right">16.47</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">4.02</td>
    <td align="right">4.36</td>
    <td align="right">4.37</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">4.99</td>
    <td align="right">5.52</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">17.06</td>
    <td align="right">15.66</td>
    <td align="right">17.41</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.79</td>
    <td align="right">4.92</td>
    <td align="right">4.92</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.84</td>
    <td align="right">8.82</td>
    <td align="right">8.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">19.54</td>
    <td align="right">18.48</td>
    <td align="right">16.31</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.36</td>
    <td align="right">5.29</td>
    <td align="right">5.42</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.18</td>
    <td align="right">13.70</td>
    <td align="right">13.69</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.54</td>
    <td align="right">23.32</td>
    <td align="right">16.69</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.37</td>
    <td align="right">5.89</td>
    <td align="right">5.89</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">11.25</td>
    <td align="right">15.64</td>
    <td align="right">15.65</td>
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
    <td align="right">2.93</td>
    <td align="right">3.26</td>
    <td align="right">3.31</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.82</td>
    <td align="right">5.08</td>
    <td align="right">5.09</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.49</td>
    <td align="right">6.69</td>
    <td align="right">6.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.46</td>
    <td align="right">3.10</td>
    <td align="right">3.16</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.43</td>
    <td align="right">5.50</td>
    <td align="right">5.50</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.12</td>
    <td align="right">10.02</td>
    <td align="right">9.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.69</td>
    <td align="right">5.84</td>
    <td align="right">3.94</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.27</td>
    <td align="right">6.30</td>
    <td align="right">6.30</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.81</td>
    <td align="right">14.25</td>
    <td align="right">14.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">5.65</td>
    <td align="right">5.74</td>
    <td align="right">3.95</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.72</td>
    <td align="right">6.57</td>
    <td align="right">6.58</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">11.87</td>
    <td align="right">17.35</td>
    <td align="right">17.33</td>
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
    <td align="right">30.20</td>
    <td align="right">18.11</td>
    <td align="right">6.58</td>
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
    <td align="right">11.76</td>
    <td align="right">11.21</td>
    <td align="right">16.83</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.63</td>
    <td align="right">4.83</td>
    <td align="right">4.80</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.74</td>
    <td align="right">6.59</td>
    <td align="right">6.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">18.42</td>
    <td align="right">17.13</td>
    <td align="right">17.58</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.40</td>
    <td align="right">5.05</td>
    <td align="right">5.22</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.17</td>
    <td align="right">9.84</td>
    <td align="right">9.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.68</td>
    <td align="right">23.77</td>
    <td align="right">17.90</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.56</td>
    <td align="right">6.44</td>
    <td align="right">6.86</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">11.01</td>
    <td align="right">15.15</td>
    <td align="right">15.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">42.45</td>
    <td align="right">40.03</td>
    <td align="right">19.43</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">10.32</td>
    <td align="right">9.27</td>
    <td align="right">8.71</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">14.31</td>
    <td align="right">18.49</td>
    <td align="right">19.86</td>
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
    <td align="right">3.45</td>
    <td align="right">3.92</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.52</td>
    <td align="right">5.70</td>
    <td align="right">5.74</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.26</td>
    <td align="right">7.64</td>
    <td align="right">7.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.75</td>
    <td align="right">3.41</td>
    <td align="right">3.39</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">5.81</td>
    <td align="right">5.83</td>
    <td align="right">5.83</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.85</td>
    <td align="right">10.69</td>
    <td align="right">10.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.02</td>
    <td align="right">7.64</td>
    <td align="right">5.18</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.59</td>
    <td align="right">7.72</td>
    <td align="right">7.47</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.84</td>
    <td align="right">15.60</td>
    <td align="right">15.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">11.73</td>
    <td align="right">10.32</td>
    <td align="right">7.55</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">9.53</td>
    <td align="right">12.03</td>
    <td align="right">14.22</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.53</td>
    <td align="right">21.92</td>
    <td align="right">22.00</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
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
    <td align="right">26.40</td>
    <td align="right">4.08</td>
    <td align="right">3.35</td>
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
    <td align="right">9.34</td>
    <td align="right">8.87</td>
    <td align="right">15.33</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.32</td>
    <td align="right">4.07</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.04</td>
    <td align="right">3.57</td>
    <td align="right">3.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.68</td>
    <td align="right">13.27</td>
    <td align="right">16.60</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">3.84</td>
    <td align="right">4.56</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.70</td>
    <td align="right">3.39</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.35</td>
    <td align="right">16.77</td>
    <td align="right">15.81</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">4.34</td>
    <td align="right">5.08</td>
    <td align="right">5.10</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.64</td>
    <td align="right">6.47</td>
    <td align="right">6.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.08</td>
    <td align="right">20.68</td>
    <td align="right">16.03</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">4.83</td>
    <td align="right">5.89</td>
    <td align="right">5.86</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.88</td>
    <td align="right">6.92</td>
    <td align="right">6.92</td>
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
    <td align="right">2.57</td>
    <td align="right">2.49</td>
    <td align="right">2.50</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">3.90</td>
    <td align="right">4.70</td>
    <td align="right">4.59</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.18</td>
    <td align="right">3.52</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.14</td>
    <td align="right">2.25</td>
    <td align="right">2.26</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">4.49</td>
    <td align="right">5.27</td>
    <td align="right">5.28</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.72</td>
    <td align="right">3.74</td>
    <td align="right">3.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.18</td>
    <td align="right">4.43</td>
    <td align="right">3.15</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">4.96</td>
    <td align="right">6.01</td>
    <td align="right">6.02</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.88</td>
    <td align="right">6.26</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.18</td>
    <td align="right">4.39</td>
    <td align="right">3.20</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.84</td>
    <td align="right">3.33</td>
    <td align="right">3.31</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.29</td>
    <td align="right">7.01</td>
    <td align="right">7.22</td>
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
    <td align="right">31.89</td>
    <td align="right">15.37</td>
    <td align="right">6.06</td>
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
    <td align="right">10.42</td>
    <td align="right">8.81</td>
    <td align="right">15.22</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.56</td>
    <td align="right">4.36</td>
    <td align="right">4.23</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.34</td>
    <td align="right">3.85</td>
    <td align="right">3.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">15.00</td>
    <td align="right">14.36</td>
    <td align="right">16.58</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">4.10</td>
    <td align="right">4.78</td>
    <td align="right">4.92</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.89</td>
    <td align="right">3.55</td>
    <td align="right">3.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">19.72</td>
    <td align="right">19.38</td>
    <td align="right">16.52</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">5.27</td>
    <td align="right">5.86</td>
    <td align="right">6.34</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">6.48</td>
    <td align="right">7.37</td>
    <td align="right">7.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">32.24</td>
    <td align="right">33.91</td>
    <td align="right">17.14</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">6.81</td>
    <td align="right">7.66</td>
    <td align="right">8.06</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">7.54</td>
    <td align="right">9.30</td>
    <td align="right">9.08</td>
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
    <td align="right">2.89</td>
    <td align="right">2.84</td>
    <td align="right">2.87</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">4.25</td>
    <td align="right">5.03</td>
    <td align="right">4.92</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.53</td>
    <td align="right">3.84</td>
    <td align="right">3.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.32</td>
    <td align="right">2.41</td>
    <td align="right">2.41</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">4.77</td>
    <td align="right">5.51</td>
    <td align="right">5.65</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.93</td>
    <td align="right">3.97</td>
    <td align="right">4.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.09</td>
    <td align="right">5.75</td>
    <td align="right">3.99</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">5.68</td>
    <td align="right">6.82</td>
    <td align="right">6.77</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">6.69</td>
    <td align="right">7.13</td>
    <td align="right">7.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">6.15</td>
    <td align="right">6.52</td>
    <td align="right">4.59</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">4.19</td>
    <td align="right">4.97</td>
    <td align="right">4.69</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">8.07</td>
    <td align="right">9.45</td>
    <td align="right">9.81</td>
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
    <td align="right">22.11</td>
    <td align="right">4.47</td>
    <td align="right">3.41</td>
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
    <td align="right">7.28</td>
    <td align="right">5.16</td>
    <td align="right">12.02</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.43</td>
    <td align="right">1.32</td>
    <td align="right">1.33</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.62</td>
    <td align="right">1.87</td>
    <td align="right">1.89</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.91</td>
    <td align="right">7.48</td>
    <td align="right">13.20</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.52</td>
    <td align="right">1.44</td>
    <td align="right">1.44</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.34</td>
    <td align="right">2.09</td>
    <td align="right">2.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.09</td>
    <td align="right">9.26</td>
    <td align="right">11.91</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.98</td>
    <td align="right">1.96</td>
    <td align="right">1.69</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.45</td>
    <td align="right">3.64</td>
    <td align="right">3.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.89</td>
    <td align="right">12.65</td>
    <td align="right">12.83</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.11</td>
    <td align="right">2.23</td>
    <td align="right">2.77</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">5.42</td>
    <td align="right">4.38</td>
    <td align="right">4.27</td>
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
    <td align="right">2.18</td>
    <td align="right">1.93</td>
    <td align="right">1.88</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.75</td>
    <td align="right">1.43</td>
    <td align="right">1.43</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.53</td>
    <td align="right">1.94</td>
    <td align="right">1.96</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.66</td>
    <td align="right">1.50</td>
    <td align="right">1.52</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.81</td>
    <td align="right">1.56</td>
    <td align="right">1.57</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.12</td>
    <td align="right">2.50</td>
    <td align="right">2.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.29</td>
    <td align="right">2.73</td>
    <td align="right">1.97</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">1.94</td>
    <td align="right">1.76</td>
    <td align="right">1.77</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.53</td>
    <td align="right">3.26</td>
    <td align="right">3.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">3.17</td>
    <td align="right">3.22</td>
    <td align="right">1.90</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.28</td>
    <td align="right">1.79</td>
    <td align="right">1.71</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.12</td>
    <td align="right">4.28</td>
    <td align="right">4.47</td>
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
    <td align="right">37.27</td>
    <td align="right">18.18</td>
    <td align="right">12.17</td>
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
    <td align="right">14.14</td>
    <td align="right">10.47</td>
    <td align="right">20.24</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">3.61</td>
    <td align="right">4.30</td>
    <td align="right">4.60</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.50</td>
    <td align="right">3.70</td>
    <td align="right">4.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">25.73</td>
    <td align="right">26.44</td>
    <td align="right">26.54</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">6.52</td>
    <td align="right">6.52</td>
    <td align="right">7.08</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.41</td>
    <td align="right">10.48</td>
    <td align="right">8.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">47.48</td>
    <td align="right">44.00</td>
    <td align="right">27.10</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">14.74</td>
    <td align="right">13.42</td>
    <td align="right">9.55</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">16.75</td>
    <td align="right">16.21</td>
    <td align="right">15.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">72.32</td>
    <td align="right">61.79</td>
    <td align="right">28.66</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">12.10</td>
    <td align="right">10.78</td>
    <td align="right">11.66</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">21.70</td>
    <td align="right">20.69</td>
    <td align="right">20.54</td>
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
    <td align="right">3.07</td>
    <td align="right">4.14</td>
    <td align="right">5.24</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.07</td>
    <td align="right">3.22</td>
    <td align="right">4.09</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.00</td>
    <td align="right">4.81</td>
    <td align="right">4.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">5.88</td>
    <td align="right">7.00</td>
    <td align="right">8.00</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.86</td>
    <td align="right">7.42</td>
    <td align="right">8.24</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">10.55</td>
    <td align="right">11.37</td>
    <td align="right">13.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">17.07</td>
    <td align="right">12.61</td>
    <td align="right">9.21</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">9.99</td>
    <td align="right">10.37</td>
    <td align="right">9.22</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">16.44</td>
    <td align="right">14.40</td>
    <td align="right">14.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">13.75</td>
    <td align="right">15.09</td>
    <td align="right">9.08</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">10.09</td>
    <td align="right">9.45</td>
    <td align="right">9.21</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">21.51</td>
    <td align="right">20.97</td>
    <td align="right">14.86</td>
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
    <td align="right">34.85</td>
    <td align="right">5.62</td>
    <td align="right">3.46</td>
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
    <td align="right">11.92</td>
    <td align="right">12.45</td>
    <td align="right">16.92</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.79</td>
    <td align="right">4.19</td>
    <td align="right">4.21</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.84</td>
    <td align="right">5.55</td>
    <td align="right">5.52</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.53</td>
    <td align="right">17.52</td>
    <td align="right">17.50</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">6.92</td>
    <td align="right">4.72</td>
    <td align="right">4.87</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.63</td>
    <td align="right">8.49</td>
    <td align="right">8.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.46</td>
    <td align="right">21.37</td>
    <td align="right">16.83</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.66</td>
    <td align="right">5.27</td>
    <td align="right">5.27</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.17</td>
    <td align="right">10.88</td>
    <td align="right">10.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">30.82</td>
    <td align="right">26.95</td>
    <td align="right">17.47</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.86</td>
    <td align="right">6.09</td>
    <td align="right">5.87</td>
    <td align="center">14</td>
    <td align="right">0.0163</td>
    <td align="right">18.17</td>
    <td align="right">14.17</td>
    <td align="right">14.25</td>
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
    <td align="right">3.35</td>
    <td align="right">3.91</td>
    <td align="right">3.92</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.94</td>
    <td align="right">5.23</td>
    <td align="right">5.24</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.15</td>
    <td align="right">5.54</td>
    <td align="right">5.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.84</td>
    <td align="right">4.81</td>
    <td align="right">4.05</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.01</td>
    <td align="right">5.95</td>
    <td align="right">5.82</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.65</td>
    <td align="right">8.66</td>
    <td align="right">7.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.93</td>
    <td align="right">7.06</td>
    <td align="right">5.36</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.25</td>
    <td align="right">6.54</td>
    <td align="right">6.53</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">15.88</td>
    <td align="right">10.38</td>
    <td align="right">10.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0304</td>
    <td align="right">4.89</td>
    <td align="right">7.01</td>
    <td align="right">5.38</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.37</td>
    <td align="right">7.34</td>
    <td align="right">7.33</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">18.81</td>
    <td align="right">12.49</td>
    <td align="right">13.43</td>
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
    <td align="right">41.89</td>
    <td align="right">21.44</td>
    <td align="right">7.53</td>
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
    <td align="right">14.58</td>
    <td align="right">13.10</td>
    <td align="right">17.68</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.01</td>
    <td align="right">4.49</td>
    <td align="right">4.57</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.23</td>
    <td align="right">6.30</td>
    <td align="right">6.44</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">23.40</td>
    <td align="right">20.17</td>
    <td align="right">18.58</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">9.08</td>
    <td align="right">5.49</td>
    <td align="right">5.66</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">17.13</td>
    <td align="right">10.88</td>
    <td align="right">10.95</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">46.34</td>
    <td align="right">44.54</td>
    <td align="right">19.16</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.52</td>
    <td align="right">7.33</td>
    <td align="right">8.51</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">25.36</td>
    <td align="right">17.57</td>
    <td align="right">18.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">78.08</td>
    <td align="right">61.86</td>
    <td align="right">22.86</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">16.43</td>
    <td align="right">11.12</td>
    <td align="right">14.34</td>
    <td align="center">14</td>
    <td align="right">0.0153</td>
    <td align="right">31.03</td>
    <td align="right">23.49</td>
    <td align="right">26.51</td>
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
    <td align="right">3.96</td>
    <td align="right">4.23</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.96</td>
    <td align="right">5.58</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.54</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.43</td>
    <td align="right">5.36</td>
    <td align="right">4.71</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.47</td>
    <td align="right">6.68</td>
    <td align="right">6.71</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">18.18</td>
    <td align="right">10.49</td>
    <td align="right">10.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">9.34</td>
    <td align="right">12.43</td>
    <td align="right">10.38</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">13.60</td>
    <td align="right">8.10</td>
    <td align="right">7.27</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">19.67</td>
    <td align="right">12.92</td>
    <td align="right">13.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0276</td>
    <td align="right">12.68</td>
    <td align="right">12.65</td>
    <td align="right">9.75</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">14.50</td>
    <td align="right">10.36</td>
    <td align="right">14.10</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">29.96</td>
    <td align="right">20.10</td>
    <td align="right">17.65</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">60.61</td>
    <td align="right">29.57</td>
    <td align="right">14.09</td>
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
    <td align="right">2.1546</td>
    <td align="right">27.00</td>
    <td align="right">41.50</td>
    <td align="right">36.01</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.39</td>
    <td align="right">15.85</td>
    <td align="right">15.92</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.31</td>
    <td align="right">20.49</td>
    <td align="right">20.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.11</td>
    <td align="right">63.49</td>
    <td align="right">39.21</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.35</td>
    <td align="right">19.46</td>
    <td align="right">19.30</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.29</td>
    <td align="right">26.66</td>
    <td align="right">26.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.42</td>
    <td align="right">77.59</td>
    <td align="right">38.22</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.38</td>
    <td align="right">18.65</td>
    <td align="right">18.55</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">28.92</td>
    <td align="right">33.39</td>
    <td align="right">33.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">56.26</td>
    <td align="right">96.16</td>
    <td align="right">37.46</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.25</td>
    <td align="right">18.82</td>
    <td align="right">18.83</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">35.33</td>
    <td align="right">37.73</td>
    <td align="right">37.78</td>
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
    <td align="right">2.7635</td>
    <td align="right">10.54</td>
    <td align="right">13.61</td>
    <td align="right">13.61</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.12</td>
    <td align="right">19.70</td>
    <td align="right">19.74</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.41</td>
    <td align="right">22.18</td>
    <td align="right">22.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">12.89</td>
    <td align="right">16.49</td>
    <td align="right">15.91</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.05</td>
    <td align="right">18.69</td>
    <td align="right">18.65</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.52</td>
    <td align="right">29.10</td>
    <td align="right">29.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">14.52</td>
    <td align="right">19.41</td>
    <td align="right">19.48</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.07</td>
    <td align="right">18.64</td>
    <td align="right">18.29</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">64.27</td>
    <td align="right">45.84</td>
    <td align="right">45.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">24.06</td>
    <td align="right">25.56</td>
    <td align="right">25.61</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.91</td>
    <td align="right">20.02</td>
    <td align="right">20.04</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.96</td>
    <td align="right">55.45</td>
    <td align="right">55.56</td>
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
    <td align="right">70.06</td>
    <td align="right">97.60</td>
    <td align="right">17.80</td>
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
    <td align="right">2.1489</td>
    <td align="right">27.64</td>
    <td align="right">42.82</td>
    <td align="right">39.27</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">12.81</td>
    <td align="right">16.14</td>
    <td align="right">16.28</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">16.68</td>
    <td align="right">20.64</td>
    <td align="right">20.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">36.98</td>
    <td align="right">62.89</td>
    <td align="right">40.59</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">17.44</td>
    <td align="right">19.69</td>
    <td align="right">19.55</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">21.44</td>
    <td align="right">25.89</td>
    <td align="right">25.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">44.71</td>
    <td align="right">77.40</td>
    <td align="right">39.24</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">17.62</td>
    <td align="right">19.50</td>
    <td align="right">18.91</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.78</td>
    <td align="right">35.23</td>
    <td align="right">34.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">60.49</td>
    <td align="right">99.95</td>
    <td align="right">39.75</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">20.14</td>
    <td align="right">21.16</td>
    <td align="right">21.13</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">38.55</td>
    <td align="right">42.71</td>
    <td align="right">43.93</td>
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
    <td align="right">2.7396</td>
    <td align="right">10.74</td>
    <td align="right">13.80</td>
    <td align="right">13.78</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">16.31</td>
    <td align="right">19.91</td>
    <td align="right">19.94</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">32.87</td>
    <td align="right">22.48</td>
    <td align="right">22.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">12.73</td>
    <td align="right">16.37</td>
    <td align="right">15.78</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">16.30</td>
    <td align="right">18.87</td>
    <td align="right">18.98</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">40.70</td>
    <td align="right">29.79</td>
    <td align="right">29.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">15.02</td>
    <td align="right">19.95</td>
    <td align="right">19.31</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">18.69</td>
    <td align="right">19.27</td>
    <td align="right">18.66</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">65.75</td>
    <td align="right">49.03</td>
    <td align="right">48.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">27.08</td>
    <td align="right">29.66</td>
    <td align="right">30.02</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">20.74</td>
    <td align="right">22.41</td>
    <td align="right">21.62</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">82.22</td>
    <td align="right">59.95</td>
    <td align="right">60.43</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">61.70</td>
    <td align="right">10.16</td>
    <td align="right">7.00</td>
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
    <td align="right">2.1546</td>
    <td align="right">13.58</td>
    <td align="right">22.26</td>
    <td align="right">26.36</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">9.38</td>
    <td align="right">12.24</td>
    <td align="right">12.08</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.32</td>
    <td align="right">15.87</td>
    <td align="right">15.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.28</td>
    <td align="right">33.85</td>
    <td align="right">28.66</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">11.39</td>
    <td align="right">14.05</td>
    <td align="right">13.99</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.15</td>
    <td align="right">22.24</td>
    <td align="right">22.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">24.77</td>
    <td align="right">47.24</td>
    <td align="right">29.64</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">13.49</td>
    <td align="right">15.16</td>
    <td align="right">15.30</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.80</td>
    <td align="right">31.92</td>
    <td align="right">31.73</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.41</td>
    <td align="right">60.34</td>
    <td align="right">30.09</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">14.46</td>
    <td align="right">16.24</td>
    <td align="right">16.20</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">29.86</td>
    <td align="right">36.84</td>
    <td align="right">36.91</td>
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
    <td align="right">2.7635</td>
    <td align="right">6.96</td>
    <td align="right">9.30</td>
    <td align="right">9.32</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">11.67</td>
    <td align="right">13.81</td>
    <td align="right">13.34</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.23</td>
    <td align="right">16.34</td>
    <td align="right">16.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.48</td>
    <td align="right">13.86</td>
    <td align="right">13.91</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">13.48</td>
    <td align="right">15.22</td>
    <td align="right">15.23</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.42</td>
    <td align="right">22.12</td>
    <td align="right">21.36</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">12.94</td>
    <td align="right">16.97</td>
    <td align="right">17.02</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">14.50</td>
    <td align="right">16.33</td>
    <td align="right">15.84</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.47</td>
    <td align="right">30.39</td>
    <td align="right">30.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0297</td>
    <td align="right">16.32</td>
    <td align="right">21.91</td>
    <td align="right">21.74</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">15.80</td>
    <td align="right">17.55</td>
    <td align="right">17.36</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">32.93</td>
    <td align="right">35.59</td>
    <td align="right">35.54</td>
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
    <td align="right">71.64</td>
    <td align="right">40.57</td>
    <td align="right">9.71</td>
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
    <td align="right">2.1489</td>
    <td align="right">13.87</td>
    <td align="right">22.64</td>
    <td align="right">27.82</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">9.43</td>
    <td align="right">12.30</td>
    <td align="right">12.43</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.79</td>
    <td align="right">16.26</td>
    <td align="right">16.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.19</td>
    <td align="right">34.03</td>
    <td align="right">29.09</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">11.79</td>
    <td align="right">13.64</td>
    <td align="right">13.69</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.82</td>
    <td align="right">21.90</td>
    <td align="right">22.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">24.36</td>
    <td align="right">46.35</td>
    <td align="right">29.59</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">13.35</td>
    <td align="right">14.71</td>
    <td align="right">14.78</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.57</td>
    <td align="right">32.07</td>
    <td align="right">32.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">30.94</td>
    <td align="right">59.51</td>
    <td align="right">29.64</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">14.10</td>
    <td align="right">15.52</td>
    <td align="right">15.64</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">29.47</td>
    <td align="right">36.31</td>
    <td align="right">36.26</td>
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
    <td align="right">2.7396</td>
    <td align="right">7.14</td>
    <td align="right">9.33</td>
    <td align="right">9.37</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">11.79</td>
    <td align="right">13.90</td>
    <td align="right">13.87</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.27</td>
    <td align="right">17.40</td>
    <td align="right">17.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.18</td>
    <td align="right">13.85</td>
    <td align="right">13.83</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">13.33</td>
    <td align="right">15.01</td>
    <td align="right">14.98</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.86</td>
    <td align="right">21.98</td>
    <td align="right">21.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">13.20</td>
    <td align="right">16.69</td>
    <td align="right">16.67</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">14.21</td>
    <td align="right">16.23</td>
    <td align="right">16.22</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">25.72</td>
    <td align="right">30.91</td>
    <td align="right">30.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0284</td>
    <td align="right">16.09</td>
    <td align="right">20.99</td>
    <td align="right">20.95</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">15.36</td>
    <td align="right">17.21</td>
    <td align="right">17.19</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">32.84</td>
    <td align="right">34.72</td>
    <td align="right">34.59</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">40.46</td>
    <td align="right">8.53</td>
    <td align="right">6.59</td>
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
    <td align="right">2.1546</td>
    <td align="right">54.58</td>
    <td align="right">51.83</td>
    <td align="right">35.84</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">18.09</td>
    <td align="right">17.43</td>
    <td align="right">20.51</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">19.94</td>
    <td align="right">39.61</td>
    <td align="right">39.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">84.97</td>
    <td align="right">79.01</td>
    <td align="right">39.92</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">20.43</td>
    <td align="right">18.83</td>
    <td align="right">21.23</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">24.72</td>
    <td align="right">58.54</td>
    <td align="right">56.46</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">105.70</td>
    <td align="right">96.90</td>
    <td align="right">38.46</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">21.51</td>
    <td align="right">19.08</td>
    <td align="right">20.57</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">36.43</td>
    <td align="right">77.52</td>
    <td align="right">77.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">135.32</td>
    <td align="right">123.03</td>
    <td align="right">40.09</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">23.80</td>
    <td align="right">20.91</td>
    <td align="right">21.34</td>
    <td align="center">14</td>
    <td align="right">0.0149</td>
    <td align="right">42.09</td>
    <td align="right">92.79</td>
    <td align="right">92.94</td>
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
    <td align="right">2.7253</td>
    <td align="right">16.28</td>
    <td align="right">23.73</td>
    <td align="right">23.75</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">21.97</td>
    <td align="right">22.02</td>
    <td align="right">24.79</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">22.93</td>
    <td align="right">40.26</td>
    <td align="right">40.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">15.99</td>
    <td align="right">32.43</td>
    <td align="right">23.83</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">23.21</td>
    <td align="right">23.72</td>
    <td align="right">25.01</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">29.64</td>
    <td align="right">56.80</td>
    <td align="right">57.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">26.37</td>
    <td align="right">54.68</td>
    <td align="right">39.04</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">25.77</td>
    <td align="right">26.21</td>
    <td align="right">27.71</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">41.70</td>
    <td align="right">76.43</td>
    <td align="right">80.47</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0262</td>
    <td align="right">24.83</td>
    <td align="right">54.74</td>
    <td align="right">36.21</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">27.16</td>
    <td align="right">28.52</td>
    <td align="right">29.60</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">47.24</td>
    <td align="right">91.56</td>
    <td align="right">92.88</td>
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
    <td align="right">58.54</td>
    <td align="right">35.16</td>
    <td align="right">10.63</td>
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
    <td align="right">2.1489</td>
    <td align="right">61.88</td>
    <td align="right">56.56</td>
    <td align="right">40.29</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">19.64</td>
    <td align="right">17.86</td>
    <td align="right">22.20</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">22.12</td>
    <td align="right">40.21</td>
    <td align="right">40.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">91.27</td>
    <td align="right">82.65</td>
    <td align="right">42.69</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">21.80</td>
    <td align="right">20.88</td>
    <td align="right">22.04</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">27.20</td>
    <td align="right">61.38</td>
    <td align="right">57.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">117.08</td>
    <td align="right">109.57</td>
    <td align="right">44.28</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">23.86</td>
    <td align="right">20.42</td>
    <td align="right">21.58</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.75</td>
    <td align="right">79.44</td>
    <td align="right">81.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">160.90</td>
    <td align="right">148.74</td>
    <td align="right">43.92</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">27.98</td>
    <td align="right">22.36</td>
    <td align="right">23.37</td>
    <td align="center">14</td>
    <td align="right">0.0158</td>
    <td align="right">46.18</td>
    <td align="right">94.98</td>
    <td align="right">95.24</td>
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
    <td align="right">2.7254</td>
    <td align="right">16.85</td>
    <td align="right">28.57</td>
    <td align="right">28.47</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">23.83</td>
    <td align="right">24.33</td>
    <td align="right">27.76</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">25.66</td>
    <td align="right">41.02</td>
    <td align="right">41.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">16.31</td>
    <td align="right">35.93</td>
    <td align="right">27.26</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">25.74</td>
    <td align="right">26.61</td>
    <td align="right">27.48</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">32.14</td>
    <td align="right">57.35</td>
    <td align="right">57.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">30.67</td>
    <td align="right">73.55</td>
    <td align="right">54.40</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">38.27</td>
    <td align="right">34.53</td>
    <td align="right">36.04</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">50.59</td>
    <td align="right">83.14</td>
    <td align="right">87.74</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0287</td>
    <td align="right">47.83</td>
    <td align="right">95.78</td>
    <td align="right">72.78</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">42.99</td>
    <td align="right">45.78</td>
    <td align="right">46.96</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">81.88</td>
    <td align="right">122.32</td>
    <td align="right">127.17</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
